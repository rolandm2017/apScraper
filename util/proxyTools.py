from dotenv import load_dotenv
import os

from ..api.proxyAPI import ProxyAPI

load_dotenv()


class ProxyTools:
    def __init__(self):
        pass



    def get_proxy_ip(self, choice):
        token = os.environ.get("apikey")
        r = ProxyAPI().get_proxy_connection_info(token)
        selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
        selected_proxy_port = r.json()["results"][choice]["port"]
        print(selected_proxy_ip)
        return selected_proxy_ip, selected_proxy_port

    def create_proxy_dict(self, ip, port):
        username = os.environ.get("username")
        password = os.environ.get("password")
        http_proxy_string = f"http://{username}:{password}@{ip}:{port}"
        # http_proxy_string = "http://" + str(ip) + ":" + str(port)
        # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy_dict = {"http": http_proxy_string, "https": http_proxy_string}
        return proxy_dict

    def confirm_public_ip(self, proxy_dict, desired_ip):
        print(proxy_dict, desired_ip, "5rm")
        r, r2 = ProxyAPI().get_public_ip(proxy_dict)
        print(desired_ip, r.text, r2.text, "6rm")
        ip_is_correct = r.text == desired_ip and r2.text == desired_ip
        return ip_is_correct


