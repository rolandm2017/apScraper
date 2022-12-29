from celery import Celery

from .config import Config

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper.Provider import Provider
from canadaAps.api.websitesAPI import WebsitesAPI
from canadaAps.api.internalAPI import InternalAPI
# from . import scraper.scraper.Scraper

from canadaAps.scraper.ProgramInit import create_app

type = "rentSeeker"

celery = Celery(type, broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)

application = create_app(celery)
print("name", __name__)

p = type
provider = Provider(p)

internal_api = InternalAPI(provider)
websites_api = WebsitesAPI()

scraper = Scraper(provider, internal_api, websites_api)

if __name__ == '__main__':
    application.run()


# flask run -h localhost -p 5000
