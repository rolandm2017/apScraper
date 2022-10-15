import os
from flask import Flask, render_template
from celery import Celery
from ..config.config import Config
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

from ..blueprints.activate import activate_blueprint
from ..blueprints.publicIp import show_public_ip_blueprint
from ..blueprints.test import test_blueprint
from ..blueprints.oneShot import one_shot_scrape_blueprint
from ..blueprints.healthCheck import health_check_blueprint


# # todo: make the same celery usable over multiple files

### Instantiate Celery ###
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)  # NEW!!!!!

### Application Factory ###
def create_app():

    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
    # app.config = "test"

    # Configure celery
    celery.conf.update(app.config)

    # make Celery available via current_app
    app.celery = celery  # https://stackoverflow.com/questions/59632556/importing-celery-in-flask-blueprints

    # Register blueprints
    register_blueprints(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_blueprints(app):
    app.register_blueprint(activate_blueprint)
    app.register_blueprint(show_public_ip_blueprint)
    app.register_blueprint(test_blueprint)
    app.register_blueprint(one_shot_scrape_blueprint)
    app.register_blueprint(health_check_blueprint)

    # app.register_blueprint(auth_blueprint, url_prefix='/users')


def register_error_handlers(app):
  pass


def configure_logging(app):
  pass