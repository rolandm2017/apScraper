from flask import Blueprint, request, render_template, abort

from ..scrapers.Scraper import Scraper
from ..scrapers.Task import Task

one_shot_scrape_blueprint = Blueprint('one_shot_scrape_blueprint', __name__)


@one_shot_scrape_blueprint.route("/", methods=["POST"])
def scrape():
    # return "scraping..."
    scrape_details = request.json

    provider = scrape_details["provider"]

    scraper = Scraper(provider)
    scraper.refresh_proxy()

    task = Task(scrape_details["id"], scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])

    results = scraper.scrape(task)
    return results
