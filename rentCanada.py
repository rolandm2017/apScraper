# from dotenv import load_dotenv

from .scrapers.Scraper import Scraper
from .scrapers.Provider import Provider

from .scrapers.ProgramInit import create_app

application = create_app()

celery = application.celery

#
# if __name__ == '__main__':
#   application.run()

### the end of it

#
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)

p = "rentCanada"
provider = Provider(p)
scraper = Scraper(provider)

# app = Flask(__name__)


if __name__ == '__main__':
    application.run()


# flask run -h localhost -p 5000
