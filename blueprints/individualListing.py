from flask import Blueprint, request, render_template, abort

from ..scrapers.Scraper import Scraper
from ..scrapers.Task import Task
from ..scrapers.Provider import Provider

from ..api.internalAPI import InternalAPI
from ..api.websitesAPI import WebsitesAPI

individual_listing_blueprint = Blueprint('individual_listing_blueprint', __name__)


@individual_listing_blueprint.route("/", methods=["POST"])
def scrape():
    # Works for RentCanada so far
    scrape_details = request.json

    provider = scrape_details["provider"]
    listing_id = scrape_details["id"]
    p = Provider(provider)

    websites_api = WebsitesAPI()
    internal_api = InternalAPI(p)

    scraper = Scraper(p, internal_api, websites_api)
    scraper.refresh_proxy()

    results = scraper.get_listing_by_id(listing_id)
    return results
