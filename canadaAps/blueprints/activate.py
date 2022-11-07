from flask import Blueprint, request

from canadaAps.scrapers.Scraper import Scraper
from canadaAps.scrapers.Provider import Provider

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI

from ..celeryTasks.celeryTasks import scrape_stuff

activate_blueprint = Blueprint('activate_blueprint', __name__)



@activate_blueprint.route("/activate", methods=["POST"])
def main():
    print("activated", request.args.to_dict())
    # print(current_app.config.get("provider"))
    provider = request.json["provider"]
    # provider = request.args.to_dict()["provider"]
    print(provider, "21rm")
    provider = Provider(provider)

    websites_api = WebsitesAPI()
    internal_api = InternalAPI(provider)
    scraper = Scraper(provider, internal_api, websites_api)

    scraper.refresh_proxy()
    print(scraper.provider, scraper.provider.type)
    tasks = scraper.ask_for_tasks()
    print("TASKS: " + str(len(tasks)))
    added_tasks = []
    for i in range(0, len(tasks)):
        async_request = scrape_stuff.apply_async(args=[scraper, tasks[i]])
        added_tasks.append(async_request.id)
    return added_tasks
        # for index in range(0, MAX_RETRIES):
        #     scrape = scraper.scrape(tasks[i])
        #     scrape_was_successful = len(scrape) > 0
        #     if scrape_was_successful:
        #         scraper.report_apartments(scrape)
        #         tasks[i].mark_complete()
        #         scraper.reset()
        #         break
        #     else:
        #         # todo: determine type of failure. "is banned?" "429?"
        #         scraper.add_failure_to_logs(scrape.issues)
        #         if index is END_OF_LOOP:
        #             scraper.report_failure_for(tasks[i])
