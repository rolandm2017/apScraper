from bson.json_util import dumps
from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from canadaAps.scraper.Task import Task
from canadaAps.scraper.MongoLogger import get_mongo_client

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

@test_blueprint.route("/test2")
def test2():
    client = get_mongo_client()
    db = client["cel_logs"]
    collection_name = db["scans"]
    flog1 = make_fake_log(5, "rentUSA", 5, 55)
    flog2 = make_fake_log(6, "rentUSA", 6, 60)
    flog3 = make_fake_log(7, "rentUSA", 7, 70)
    collection_name.insert_one(flog1)
    collection_name.insert_many([flog2, flog3])
    return "done"

@test_blueprint.route("/test3")
def test3():
    client = get_mongo_client()
    db = client["cel_logs"]
    collection_name = db["scans"]
    docs = collection_name.find()
    d = []
    for doc in docs:
        d.append(convert_doc_to_dict(doc))
    return d

def convert_doc_to_dict(doc):
    print(doc, '50rm')
    return {
        "task_id": doc["task_id"],
        "provider": doc["provider"],
        "lat": doc["lat"],
        "long": doc["long"]
    }

def make_fake_log(task_id, provider, lat, long):
    return {"task_id": task_id, "provider": provider, "lat": lat, "long": long}


@test_blueprint.route("/check_pretend")
def get_pretend_tasks():
    celery = current_celery_app
    # current_app.
    i = celery.control.inspect()
    scheduled = i.scheduled()
    active = i.active()
    reserved = i.reserved()

    return {"active": active, "reserved": reserved, "scheduled": scheduled}

