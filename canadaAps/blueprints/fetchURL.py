from flask import Blueprint, request

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Provider import Provider

from canadaAps.api.internalAPI import InternalAPI
from canadaAps.api.websitesAPI import WebsitesAPI

from ..celeryTasks.celeryTasks import scrape_stuff

fetch_url_blueprint = Blueprint('fetch_url', __name__)


@fetch_url_blueprint.route("/fetch-url")
def fetch_url():
    id_for_missing_url = request.args.get("id")
    print("trying to get url for id:", id_for_missing_url)

    provider_object = Provider("rentCanada")  # this route is always rentCanada
    websites_api = WebsitesAPI()
    internal_api = InternalAPI(provider_object)
    scraper = Scraper(provider_object, internal_api, websites_api)
    scraper.refresh_proxy()

    # get the url for the id
    url = scraper.get_missing_url_for_id(id_for_missing_url)
    print("returning url:", url, "...for id:", id_for_missing_url)
    return url
