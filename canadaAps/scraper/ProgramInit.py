import os
from flask import Flask
from canadaAps.config import Config, DevelopmentConfig

from canadaAps.blueprints.activate import activate_blueprint
from canadaAps.blueprints.publicIp import show_public_ip_blueprint
from canadaAps.blueprints.test import test_blueprint
from canadaAps.blueprints.oneShot import one_shot_scrape_blueprint
from canadaAps.blueprints.healthCheck import health_check_blueprint
from canadaAps.blueprints.fetchURL import fetch_url_blueprint
from canadaAps.blueprints.purgeCelery import purge_blueprint
from canadaAps.blueprints.inspectQueue import inspect_queue_blueprint
from canadaAps.blueprints.logging import logging_blueprint


# # todo: make the same celery usable over multiple files

# ### Instantiate Celery ###
print("Name:", __name__)  # todo: change "rentCanada" to imported line
# celery = Celery("rentCanada", broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)


# ### Application Factory ###
def create_app(celery):

    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    if CONFIG_TYPE == "config.DevelopmentConfig":
        c = DevelopmentConfig
    else:
        c = Config
    app.config.from_object(c)

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
    app.register_blueprint(fetch_url_blueprint)
    app.register_blueprint(purge_blueprint)
    app.register_blueprint(inspect_queue_blueprint)
    app.register_blueprint(logging_blueprint)


def register_error_handlers(app):
    pass


def configure_logging(app):
    pass