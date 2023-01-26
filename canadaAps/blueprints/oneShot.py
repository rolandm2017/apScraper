from flask import Blueprint, request
import json

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

    results, num_of_results = scraper.scrape(task)
    print("\n\n\n\n\n\n\n\n\n\n\n\n======\n\n--\n\n--\n\n--")
    print(results, num_of_results, '35rm')
    # formatted json output
    # print(results.get_results(), '35rm')
    # print(json.dumps(results, indent=4))
    print("return payload: 34rm")
    # the_goods = results["results"]
    # print(the_goods, '37rm')
    # raise ValueError("pause")
    if provider is Provider.rentCanada:
        # has to be this way so the parser receives "unprocessed.results.listings" as the data entrypoint
        payload = {"results": {"listings": results.get_results()}}
        return payload
    elif provider is Provider.rentFaster:
        # has to be this way so the parser receives "unprocessed.results.listings" as the data entrypoint
        payload = {"results": {"listings": results.get_results()}}
        return payload
    else:
        # has to be this way so the parser receives "unprocessed.results.hits" as the data entrypoint
        payload = {"results": {"hits": results.get_results()}}
        return payload
