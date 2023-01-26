from time import sleep
from celery import current_app
import json

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Provider import Provider

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI

from canadaAps.scraper.Task import Task


MAX_RETRIES = 5
END_OF_LOOP = MAX_RETRIES - 1


@current_app.task(name="scrape_stuff")
def scrape_stuff(provider, task):
    task_json = json.loads(task)
    task = Task(task_json["identifier"], task_json["lat"], task_json["long"], task_json["viewport_width"])
    provider = Provider(provider)
    # # fixme: isnt remaking these objects over and over pretty costly?
    websites_api = WebsitesAPI()
    internal_api = InternalAPI(provider)

    scraper = Scraper(provider, internal_api, websites_api)

    scraper.refresh_proxy()
    for index in range(0, MAX_RETRIES):
        scrape, num_of_results = scraper.scrape(task)
        if scrape.success:
            scraper.report_apartments_and_mark_complete(task, scrape)
            if num_of_results == 0:
                return "Empty"
            return "success!"
        else:
            # todo: determine type of failure. "is banned?" "429?"
            scraper.add_failure_to_logs(scrape)
            if index is END_OF_LOOP:
                scraper.report_failure_for(task)
                scraper.reset_logs()
                return "failure!"
