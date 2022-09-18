from flask import Blueprint, render_template, abort
from ..proxyTools.ipgetter import get_proxy_ip
from ..proxyTools.checker import confirm_public_ip

show_public_ip_blueprint = Blueprint('show_public_ip_blueprint', __name__)

@show_public_ip_blueprint.route("/public_ip")
def show_public_ip():
    # FIXME: Its a function called "show_public_ip" that returns the proxy ip.
    # FIXME: It needs to implement a request to the ip checker api via a proxied request.
    proxy_ip = get_proxy_ip(0)
    print(proxy_ip)
    return proxy_ip
