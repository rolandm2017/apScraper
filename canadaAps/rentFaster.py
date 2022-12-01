# from dotenv import load_dotenv
from flask import Flask

from canadaAps.scraper.Scraper import Scraper
from canadaAps.scraper import Provider
from canadaAps.blueprints.publicIp import show_public_ip_blueprint
from canadaAps.blueprints.test import test_blueprint
from canadaAps.blueprints.oneShot import one_shot_scrape_blueprint


p = "rentFaster"
provider = Provider(p)
scraper = Scraper(provider)



app = Flask(__name__)

app.register_blueprint(show_public_ip_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(one_shot_scrape_blueprint)


if __name__ == '__main__':
    app.run()


# flask run -h localhost -p 5000
