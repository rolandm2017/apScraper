from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from canadaAps.scrapers.Task import Task

# from ..scrapers.ProgramInit import celery

# ## dont do this
# from rentCanada import application
# ##

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
    return scraper.get_results()


@test_blueprint.route("/pretend_tasks", methods=["POST"])
@shared_task(name='celery_tasks.pretend')
def pretend():
    times = request.json["pretend"]
    print(times)
    responses = []
    for t in times:
        # create_task.delay(int(t))
        # todo: attach .celery to current_app  ( i think it is now)
        print(t, "31rm")
        print(current_app, "39rm")
        async_result = current_app.celery.send_task("celery_tasks.pretend", args=[int(t)])
        print(async_result, "33rm")
        responses.append(async_result.id)
        print(type(async_result))
        # r = result_id.get()
        # print('Processing is {}'.format(r))
        # responses.append('Processing is {}'.format(r))
    return responses

@test_blueprint.route("/check_pretend")
def get_pretend_tasks():
    celery = current_celery_app
    # current_app.
    i = celery.control.inspect()
    scheduled = i.scheduled()
    active = i.active()
    reserved = i.reserved()

    print("\n=============")
    print("active:", active)
    print("reserved:", reserved)
    return {"active": active, "reserved": reserved, "scheduled": scheduled}
