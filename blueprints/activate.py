from flask import Blueprint, render_template, abort, request, current_app
from time import sleep

from scrapers.Scraper import Scraper
from scrapers.Provider import Provider

from api.internalAPI import InternalAPI
from api.websitesAPI import WebsitesAPI

activate_blueprint = Blueprint('activate_blueprint', __name__)

MAX_RETRIES = 5
END_OF_LOOP = MAX_RETRIES - 1

@activate_blueprint.route("/activate", methods=["POST"])
def main():
    print("activated")
    # print(current_app.config.get("provider"))
    provider = request.json["provider"]
    print(provider, "21rm")
    provider = Provider(provider)

    websites_api = WebsitesAPI()
    internal_api = InternalAPI(provider)
    scraper = Scraper(provider, internal_api, websites_api)

    scraper.refresh_proxy()
    print(scraper.provider, scraper.provider.type)
    tasks = scraper.ask_for_tasks()
    print("TASKS: " + str(len(tasks)))
    for i in range(0, len(tasks)):
        for index in range(0, MAX_RETRIES):
            scrape = scraper.scrape(tasks[i])
            scrape_was_successful = len(scrape) > 0
            if scrape_was_successful:
                scraper.report_apartments(scrape)
                tasks[i].mark_complete()
                scraper.reset()
                break
            else:
                # todo: determine type of failure. "is banned?" "429?"
                scraper.add_failure_to_logs(scrape.issues)
                if index is END_OF_LOOP:
                    scraper.report_failure_for(tasks[i])
