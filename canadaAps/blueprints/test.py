from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from canadaAps.scraper.Task import Task

# from ..scraper.ProgramInit import celery

test_blueprint = Blueprint('test_blueprint', __name__)


@test_blueprint.route("/test")
def test():
    scrape_details = request.json
    # task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"], queue)
    task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])
    scraper = []  # fixme: temp
    scraper.refresh_proxy()
    task.forward_task_to_scraper(scraper)
    return scraper.get_results()


@test_blueprint.route("/check_pretend")
def get_pretend_tasks():
    celery = current_celery_app
    # current_app.
    i = celery.control.inspect()
    scheduled = i.scheduled()
    active = i.active()
    reserved = i.reserved()

    return {"active": active, "reserved": reserved, "scheduled": scheduled}
