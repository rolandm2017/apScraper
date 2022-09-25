from flask import Blueprint, request

from ..scrapers.Task import Task

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route("/test")
def test():
    scrape_details = request.json
    # task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"], queue)
    task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"])
    scraper.refresh_proxy()
    task.forward_task_to_scraper(scraper)
    results = scraper.get_results()
    return results