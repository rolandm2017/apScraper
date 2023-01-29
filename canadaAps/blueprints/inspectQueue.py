from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from canadaAps.scraper.Task import Task

# from ..scraper.ProgramInit import celery

inspect_queue_blueprint = Blueprint('inspect_queue_blueprint', __name__)


@inspect_queue_blueprint.route("/inspect-queue", methods=["GET"])
def inspect_queue():
    celery = current_celery_app
    # current_app.
    # inspect_result = getattr(celery.control.inspect(), 'scheduled')()
    # return inspect_result
    i = celery.control.inspect()
    try:
        scheduled = i.scheduled()["celery@kingdom"]
        active = i.active()["celery@kingdom"]
        reserved = i.reserved()["celery@kingdom"]
        registered = i.registered()["celery@kingdom"]

        return {"active": active,
                "active_count": len(active),
                "reserved": reserved,
                "reserved_count": len(reserved),
                "scheduled": scheduled,
                "scheduled_count": len(scheduled),
                "registered": registered,
                "registered_count": len(registered)
                }
    except TypeError:
        return {"message": "Looks like celery was inactive"}


@inspect_queue_blueprint.route("/inspect-and-count", methods=["GET"])
def inspect_and_count():
    QUEUE_NAME = "rentCanada"
    celery = current_celery_app
    client = celery.connection().channel().client

    length = client.llen(QUEUE_NAME)
    return {"task_count": length}
