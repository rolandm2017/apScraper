# from dotenv import load_dotenv
from celery import Celery

# from . import Config, DevelopmentConfig
from .config import Config

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Provider import Provider
from canadaAps.api.websitesAPI import WebsitesAPI
from canadaAps.api.internalAPI import InternalAPI
# from . import scraper.scraper.Scraper

from canadaAps.scraper.ProgramInit import create_app

celery = Celery("rentCanada", broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)

application = create_app(celery)
print("name!", __name__)
#


# celery = application.celery

#
# if __name__ == '__main__':
#   application.run()

### the end of it

#
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)

p = "rentCanada"
provider = Provider(p)

internal_api = InternalAPI(provider)
websites_api = WebsitesAPI()

scraper = Scraper(provider, internal_api, websites_api)

# app = Flask(__name__)


if __name__ == '__main__':
    application.run()


# flask run -h localhost -p 5000
