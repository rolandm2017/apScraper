from flask import Blueprint, request, render_template, abort

from ..scrapers.Scraper import Scraper

one_shot_scrape_blueprint = Blueprint('one_shot_scrape_blueprint', __name__)


@one_shot_scrape_blueprint.route("/", methods=["POST"])
def scrape():
    # return "scraping..."
    scrape_details = request.json

    provider = scrape_details["provider"]

    scraper = Scraper(provider)
    scraper.refresh_proxy()

    results = scraper.scrape(scrape_details)
    print(results, "21rm")
    return results
