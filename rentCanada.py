# from dotenv import load_dotenv
from flask import Flask, request

from .scrapers.Scraper import Scraper
from .scrapers.Provider import Provider
from .blueprints.activate import activate_blueprint
from .blueprints.publicIp import show_public_ip_blueprint
from .blueprints.test import test_blueprint
from .blueprints.oneShot import one_shot_scrape_blueprint
from .blueprints.healthCheck import health_check_blueprint

# p = "rentCanada"
# provider = Provider(p)
# scraper = Scraper(provider)

app = Flask(__name__)

app.register_blueprint(activate_blueprint)
app.register_blueprint(show_public_ip_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(one_shot_scrape_blueprint)
app.register_blueprint(health_check_blueprint)

if __name__ == '__main__':
    app.run()


# flask run -h localhost -p 5000
