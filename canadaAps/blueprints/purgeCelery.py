from flask import Blueprint, request, current_app
# from celery import task
from celery import shared_task, current_app as current_celery_app

from canadaAps.scraper.Task import Task

# from ..scraper.ProgramInit import celery

purge_blueprint = Blueprint('purge_blueprint', __name__)


@purge_blueprint.route("/purge", methods=["DELETE"])
def get_pretend_tasks():
    celery = current_celery_app
    i = celery.control.purge()

    return {"purged": i}
