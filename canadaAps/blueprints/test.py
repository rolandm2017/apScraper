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


from ..celeryTasks.celeryTasks import delayed_math
@test_blueprint.route("/pretend_tasks2", methods=["POST"])
def pretend2():
    times = request.json["pretend"]
    print(times, "34rm")
    responses = []
    for t in times:
        x = delayed_math.apply_async(args=[t])
        print(x, "38rm")
        responses.append(x.id)
    return responses

# @test_blueprint.route("/pretend_tasks", methods=["POST"])
# @shared_task(name='celery_tasks.pretend')
# def pretend():
#     times = request.json["pretend"]
#     responses = []
#     for t in times:
#         # async_result = current_app.celery.send_task("celery_tasks.pretend", args=[int(t)])
#         r = divide(t)
#         responses.append(r)
#         # responses.append(async_result.id)
#     return responses

@test_blueprint.route("/check_pretend")
def get_pretend_tasks():
    celery = current_celery_app
    # current_app.
    i = celery.control.inspect()
    scheduled = i.scheduled()
    active = i.active()
    reserved = i.reserved()

    return {"active": active, "reserved": reserved, "scheduled": scheduled}
