import os
import time
# from flask import current_app
from celery import shared_task

# from ..scrapers.ProgramInit import celery  # fixme: start

# todo: which folder does this go in?

# @current_app.celery.task(name="create_task")
@shared_task(name='celery_tasks.create_task')
def create_task(task_type):
    print(task_type * 20)
    return True