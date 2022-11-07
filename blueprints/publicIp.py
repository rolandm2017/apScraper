from flask import Blueprint, request
from util.proxyTools import ProxyTools

show_public_ip_blueprint = Blueprint('show_public_ip_blueprint', __name__)

@show_public_ip_blueprint.route("/public_ip")
def show_public_ip():
    request_ip = request.remote_addr
    proxy_ip, proxy_port = ProxyTools().get_proxy_ip(0)
    proxy_dict = ProxyTools().create_proxy_dict(proxy_ip, proxy_port)
    # http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
    # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
    # proxy = {"http": http_proxy_string, "https": https_proxy_string}
    public_ip_is_correct = ProxyTools().confirm_public_ip_is_proxy_ip(proxy_dict, proxy_ip)
    print(proxy_ip, public_ip_is_correct, request_ip, "15rm")
    return {"proxy_ip": proxy_ip, "proxy_works": public_ip_is_correct, "request_ip": request_ip}
    # return 200
