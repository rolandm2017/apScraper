import requests
from flask import Flask, request, make_response

app = Flask(__name__)

from .proxyTools.ipgetter import get_proxy_ip
from .proxyTools.checker import check_public_ip
from .scrapers.Scraper import Scraper

@app.route("/")
def apartments():
    """
    Uses lat and long to query RentCanada.com for apartments.
    Translation from city,state,country to lat and long must be done prior to this step.
    NOTE: In RentCanada's coordinate system, West is negative, East is positive.
    :return: A list of gyms.
    """
    scrape_details = request.json

    proxy_ip = scrape_details["proxy_ip"]
    proxy_port = scrape_details["proxy_port"]
    provider = scrape_details["provider"]

    scraper = Scraper(provider)

    results = scraper.scrape(scrape_details)
    return results

@app.route("/public_ip")
def public_ip():
    proxy_ip = get_proxy_ip(0)
    print(public_ip)
    return proxy_ip


# flask run -h localhost -p 5000
