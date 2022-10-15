from flask import Blueprint, request, current_app

from ..scrapers.Task import Task
from .tasks import create_task  # fixme: start2
# from ..scrapers.ProgramInit import celery

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route("/test")
def test():
    scrape_details = request.json
    # task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"], queue)
    task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])
    # todo: import the Scraper singleton and use it here
    # todo: make a Scraper singleton (possible?) perhaps just put it in 1 specific loc it'll always be in?
    scraper = []  # fixme: temp
    scraper.refresh_proxy()
    task.forward_task_to_scraper(scraper)
    results = scraper.get_results()
    return results


@test_blueprint.route("/pretend_tasks")
def pretend():
    times = request.json["pretend"]
    for t in times:
        # create_task.delay(int(t))
        # todo: attach .celery to current_app  ( i think it is now)
        result = current_app.celery.send_task("celery_tasks.create_task", args=[int(t)])
        r = result.get()
        print('Processing is {}'.format(r))
        return 'Processing is {}'.format(r)

# @test_blueprint.route("/check_pretend")
# def get_pretend_tasks():
#     i = celery.control.inspect()
#     active = i.active()
#     reserved = i.reserved()
#
#     print("\n\n")
#     print(active)
#     print(reserved)