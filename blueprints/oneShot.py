from flask import Blueprint, request, render_template, abort

from scrapers.Scraper import Scraper

one_shot_scrape = Blueprint('one_shot_scrape', __name__)

@one_shot_scrape.route("/")
def scrape():
    return "scraping..."
    # scrape_details = request.json
    #
    # proxy_ip = scrape_details["proxy_ip"]
    # proxy_port = scrape_details["proxy_port"]
    # provider = scrape_details["provider"]
    #
    # scraper = Scraper(provider)
    #
    # results = scraper.scrape(scrape_details)
    # return results