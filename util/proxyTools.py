from dotenv import load_dotenv
import os

from api.proxyAPI import ProxyAPI

load_dotenv()


class ProxyTools:
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_ip(choice):
        token = os.environ.get("apikey")
        r = ProxyAPI().get_proxy_connection_info(token)
        selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
        selected_proxy_port = r.json()["results"][choice]["port"]
        print(selected_proxy_ip)
        return selected_proxy_ip, selected_proxy_port

    @staticmethod
    def create_proxy_dict(ip, port):
        username = os.environ.get("username")
        password = os.environ.get("password")
        http_proxy_string = f"http://{username}:{password}@{ip}:{port}"
        # http_proxy_string = "http://" + str(ip) + ":" + str(port)
        # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy_dict = {"http": http_proxy_string, "https": http_proxy_string}
        return proxy_dict

    @staticmethod
    def confirm_public_ip_is_proxy_ip(proxy_dict, desired_ip_from_proxy):
        print(proxy_dict, desired_ip_from_proxy, "5rm")
        # test
        # token = os.environ.get("apikey")
        r, r2 = ProxyAPI().get_public_ip(proxy_dict)
        print(desired_ip_from_proxy, "35rm")
        print(r.text, "35rm")
        print(r2.text, "35rm")
        ip_is_correct = r.text == desired_ip_from_proxy and r2.text == desired_ip_from_proxy
        return ip_is_correct


