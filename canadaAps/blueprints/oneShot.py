from flask import Blueprint, request

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Task import Task
from canadaAps.scraper.Provider import Provider

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI

one_shot_scrape_blueprint = Blueprint('one_shot_scrape_blueprint', __name__)


@one_shot_scrape_blueprint.route("/", methods=["POST"])
def scrape():
    # return "scraping..."
    scrape_details = request.json

    provider = scrape_details["provider"]
    p = Provider(provider)

    websites_api = WebsitesAPI()
    internal_api = InternalAPI(p)

    scraper = Scraper(p, internal_api, websites_api)
    scraper.refresh_proxy()

    if hasattr(scrape_details, "zoomWidth"):
        task = Task(scrape_details["id"], scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])
    else:
        task = Task(scrape_details["id"], scrape_details["lat"], scrape_details["long"])

    results = scraper.scrape(task)
    print(results.results, '33rm')
    if provider is Provider.rentCanada:
        return {"results": results.results}
    elif provider is Provider.rentFaster:
        return {"results": results.results}
    else:
        return {"results": results.results}
