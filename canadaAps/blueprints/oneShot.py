from flask import Blueprint, request
import json

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Task import Task
from canadaAps.scraper.Provider import Provider

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI

from canadaAps.util.colors import bcolors

one_shot_scrape_blueprint = Blueprint('one_shot_scrape_blueprint', __name__)


@one_shot_scrape_blueprint.route("/", methods=["POST"])
def scrape():
    # return "scraping..."
    scrape_details = request.json

    provider = scrape_details["provider"]
    print("checking provider:" + provider)
    p = Provider(provider)

    websites_api = WebsitesAPI()
    internal_api = InternalAPI(p)

    scraper = Scraper(p, internal_api, websites_api)
    scraper.refresh_proxy()
    print(scrape_details, '30rm')
    task = Task(scrape_details["id"], scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])

    print("here is what the task looks like: 35rm")
    print(vars(task))
    results, num_of_results = scraper.scrape(task)
    print("\n\n======\n\n--")
    print(num_of_results, '35rm')

    print("return payload: 34rm")

    if provider is Provider.rentCanada:
        # has to be this way so the parser receives "unprocessed.results.listings" as the data entrypoint
        print(bcolors.OKBLUE + f"\n======\nsending payload for: {provider}" + bcolors.ENDC)
        payload = results.get_results()
        return payload
    elif provider is Provider.rentFaster:
        # has to be this way so the parser receives "unprocessed.results.listings" as the data entrypoint
        print(bcolors.OKBLUE + f"\n===\nending payload for: {provider}" + bcolors.ENDC)
        payload = results.get_results()
        return payload
    else:
        # has to be this way so the parser receives "unprocessed.results.hits" as the data entrypoint
        print(bcolors.OKBLUE + f"\n===\nsending payload for: {provider}" + bcolors.ENDC)
        return results.get_results()
