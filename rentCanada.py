# from dotenv import load_dotenv

from scrapers.Scraper import Scraper
from scrapers.Provider import Provider
from api.websitesAPI import WebsitesAPI
from api.internalAPI import InternalAPI

from scrapers.ProgramInit import create_app

application = create_app()
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
