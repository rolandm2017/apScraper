from flask import Blueprint, render_template, abort, request
from ..proxyTools.ipgetter import get_proxy_ip
from ..proxyTools.checker import confirm_public_ip

show_public_ip_blueprint = Blueprint('show_public_ip_blueprint', __name__)

@show_public_ip_blueprint.route("/public_ip")
def show_public_ip():
    request_ip = request.remote_addr
    proxy_ip, proxy_port = get_proxy_ip(0)
    http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
    https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
    proxy = {"http": http_proxy_string, "https": https_proxy_string}
    public_ip_is_correct = confirm_public_ip(proxy, proxy_ip)
    return (proxy_ip, public_ip_is_correct, request_ip)
