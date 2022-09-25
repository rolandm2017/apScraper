from flask import Blueprint, render_template, abort, request, current_app
from time import sleep

from ..scrapers.Scraper import Scraper
from ..scrapers.Provider import Provider

activate_blueprint = Blueprint('activate_blueprint', __name__)


@activate_blueprint.route("/activate")
def main():
    print("activated")
    # return "Activated"
    provider = Provider(current_app.config.get("provider"))
    scraper = Scraper(provider)
    print(scraper.provider, scraper.provider.type)
    task = scraper.ask_for_task()
    if task.is_ready:
        for index in range(0, 5):
            scrape = scraper.scrape(task)
            if scrape.was_successful:
                scraper.report_apartments(scrape)
                task.mark_complete(task)
                break
            else:
                # todo: determine type of failure. "is banned?" "429?"
                scraper.add_failure_to_logs(scrape.issues)
                if index < 4:
                    scraper.retry(task)
                else:
                    scraper.report_failure_for(task)
                pass
    else:
        # No task
        if scraper.queue_confirmed_empty():
            sleep(1 * 24 * 60 * 60)
        else:
            exit()
