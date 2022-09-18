# from dotenv import load_dotenv
from flask import Flask, request
from time import sleep
import os

from .proxyTools.ipgetter import get_proxy_ip
from .scrapers.Scraper import Scraper
from .scrapers.Provider import Provider
from .tasks import TaskQueue
from .tasks import Task

from .blueprints.publicIp import public_ip
# from .blueprints.test import test


p = "rentCanada"
provider = Provider(p)  # todo: turn into command line argument?
scraper = Scraper(provider)



app = Flask(__name__)

app.register_blueprint(public_ip)
# app.register_blueprint(test)

# @app.route("/pickProvider")
# def pick():
#     provider = request.json["provider"]

# @app.route("/")
# def apartments():
#     scrape_details = request.json
#
#     proxy_ip = scrape_details["proxy_ip"]
#     proxy_port = scrape_details["proxy_port"]
#     provider = scrape_details["provider"]
#
#     scraper = Scraper(provider)
#
#     results = scraper.scrape(scrape_details)
#     return results
#
# @app.route("/test")
# def test():
#     scrape_details = request.json
#     queue = TaskQueue(scrape_details["provider"])
#     task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"], queue)
#     scraper.refresh_proxy()
#     task.forward_task_to_scraper(scraper)
#     results = scraper.get_results()
#     return results

@app.route("/activate")
def main():
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

#
# @app.route("/public_ip")
# def public_ip():
#     proxy_ip = get_proxy_ip(0)
#     print(public_ip)
#     return proxy_ip

if __name__ == '__main__':
    app.run()


# flask run -h localhost -p 5000
