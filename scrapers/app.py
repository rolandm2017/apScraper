import requests
from flask import Flask, request, make_response
from time import sleep
from sys import argv

app = Flask(__name__)

from .proxyTools.ipgetter import get_proxy_ip
from .proxyTools.checker import check_public_ip
from .scrapers.Scraper import Scraper
from .scrapers.Provider import Provider

p = app.config["provider"]

provider = Provider(p)  # todo: turn into command line argument?
scraper = Scraper(provider)
scraper.init(p)

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

@app.route("/tests")
def test():
    # wherein we find out if my OOP works or not

    task = scraper.ask_for_task()
    if task.is_ready:
        for index in range(0, 5):
            scrape = scraper.scrape(task)
            if scrape.was_successful:
                scraper.report_apartments(scrape)
                task.mark_complete(task)
                scraper.queue.delete_from_queue(task)
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


@app.route("/public_ip")
def public_ip():
    proxy_ip = get_proxy_ip(0)
    print(public_ip)
    return proxy_ip

if __name__ == '__main__':
    app.config['provider'] = argv[1]
    app.run()


# flask run -h localhost -p 5000
