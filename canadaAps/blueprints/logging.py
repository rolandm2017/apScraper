from flask import Blueprint, request, current_app

from canadaAps.scraper.MongoLogger import get_scan_collection, get_all_logs, convert_doc_to_dict

logging_blueprint = Blueprint('logging_blueprint', __name__)


@logging_blueprint.route("/see-logs", methods=["GET"])
def see_logs():
    scan_coll = get_scan_collection()
    logs = get_all_logs(scan_coll)
    logs_dict = []
    for log in logs:
        # convert from ??? to dict to avoid ' assert isinstance(data, bytes), "applications must write bytes"'
        logs_dict.append(convert_doc_to_dict(log))
    return logs_dict
