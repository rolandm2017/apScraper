from flask import Blueprint

health_check_blueprint = Blueprint('health_check', __name__)


@health_check_blueprint.route("/health_check")
def health_check():
    print("Online")
    return "Online"