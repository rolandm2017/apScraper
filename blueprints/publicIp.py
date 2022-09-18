from flask import Blueprint, render_template, abort
from ..proxyTools.ipgetter import get_proxy_ip

public_ip = Blueprint('public_ip', __name__)

@public_ip.route("/public_ip")
def public_ip():
    proxy_ip = get_proxy_ip(0)
    print(public_ip)
    return proxy_ip
