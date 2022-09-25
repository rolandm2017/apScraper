# from dotenv import load_dotenv
from flask import Flask, request

from .scrapers.Scraper import Scraper
from .scrapers.Provider import Provider
from .blueprints.publicIp import show_public_ip_blueprint
from .blueprints.test import test_blueprint
from .blueprints.oneShot import one_shot_scrape_blueprint

p = "rentSeeker"
provider = Provider(p)
scraper = Scraper(provider)

app = Flask(__name__)

app.register_blueprint(show_public_ip_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(one_shot_scrape_blueprint)


if __name__ == '__main__':
    app.run()


# flask run -h localhost -p 5000
