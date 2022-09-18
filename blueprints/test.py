from flask import Blueprint, request, render_template, abort

from ..tasks import TaskQueue
from ..tasks import Task

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route("/test")
def test():
    return "test complete"
#     scrape_details = request.json
#     queue = TaskQueue(scrape_details["provider"])
#     task = Task(scrape_details["lat"], scrape_details["long"], scrape_details["zoomWidth"], queue)
#     scraper.refresh_proxy()
#     task.forward_task_to_scraper(scraper)
#     results = scraper.get_results()
#     return results