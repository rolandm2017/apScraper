from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from ..celeryTasks.celeryTasks import divide

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


from ..celeryTasks.celeryTasks import delayed_mathsss
@test_blueprint.route("/pretend_tasks2", methods=["POST"])
def pretend2():
    times = request.json["pretend"]
    print(times)
    responses = []
    for t in times:
        x = delayed_mathsss.apply_async(args=[t])
        print(x)
        responses.append(x.id)
    return responses

# @test_blueprint.route("/pretend_tasks", methods=["POST"])
# @shared_task(name='celery_tasks.pretend')
# def pretend():
#     times = request.json["pretend"]
#     print(times)
#     responses = []
#     for t in times:
#         print(t, "31rm")
#         print(current_app, "39rm")
#         # async_result = current_app.celery.send_task("celery_tasks.pretend", args=[int(t)])
#         # print(async_result, "33rm")
#         r = divide(t)
#         print(r, "43rm")
#         responses.append(r)
#         # responses.append(async_result.id)
#         # print(type(async_result))
#     return responses

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
