from simple_chalk import green, yellow, red

from time import sleep
from celery import current_app
import json

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Provider import Provider
from canadaAps.scraper.MongoLogger import write_log

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI
from canadaAps.scraper.Logger import report_progress

from canadaAps.scraper.Task import Task


MAX_RETRIES = 5
END_OF_LOOP = MAX_RETRIES - 1


@current_app.task(name="scrape_stuff")
def scrape_stuff(provider, task):
    provider_name = provider
    task_json = json.loads(task)
    task = Task(task_json["identifier"], task_json["lat"], task_json["long"], task_json["viewport_width"])
    print(report_progress("handling: " + json.dumps(task.__dict__) + " for provider: " + provider))
    provider = Provider(provider)
    # # fixme: isnt remaking these objects over and over pretty costly?
    websites_api = WebsitesAPI()
    internal_api = InternalAPI(provider)

    # put this sleep here to avoid getting 429'ed or outright IP banned by the providers
    mod_via_id_num = task.identifier % 100
    mod_via_id_num = mod_via_id_num / 4
    print("delaying for: " + str(mod_via_id_num + 5))
    sleep(5 + mod_via_id_num)

    scraper = Scraper(provider, internal_api, websites_api)

    scraper.refresh_proxy()
    for index in range(0, MAX_RETRIES):
        scrape, num_of_results = scraper.scrape(task)
        if scrape.success:
            scraper.report_apartments_and_mark_complete(task, scrape)
            # log the result
            connect_and_write_log(task.identifier, provider_name, task.lat, task.long, num_of_results)
            # report result to backend
            if num_of_results == 0:
                return str(task.identifier) + " Empty"
            return str(task.identifier) + " " + str(num_of_results) + " success!"
        else:
            # todo: determine type of failure. "is banned?" "429?"
            scraper.add_failure_to_logs(scrape)
            if index is END_OF_LOOP:
                scraper.report_failure_for(task)
                scraper.reset_logs()
                return "failure!"
