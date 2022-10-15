from flask import Flask
# from celery import Celery


import os
from flask import Flask, render_template
from celery import Celery  # NEW!!!!!
from config import Config  # NEW!!!!!
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

from ..blueprints.activate import activate_blueprint
from ..blueprints.publicIp import show_public_ip_blueprint
from ..blueprints.test import test_blueprint
from ..blueprints.oneShot import one_shot_scrape_blueprint
from ..blueprints.healthCheck import health_check_blueprint


# # todo: make the same celery usable over multiple files
# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["CELERY_CONFIG"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


