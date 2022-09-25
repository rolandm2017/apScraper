import os
from dotenv import load_dotenv
import requests

load_dotenv()


class ProxyTools:
    def __init__(self):
        pass

    def create_proxy_dict(self, ip, port):
        http_proxy_string = "http://" + str(ip) + ":" + str(port)
        # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy_dict = {"http": http_proxy_string, "https": http_proxy_string}
        return proxy_dict
    def get_proxy_ip(self, choice):
        token = os.environ.get("apikey")
        r = ProxyAPI().get_proxy_connection_info(token)
        selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
        selected_proxy_port = r.json()["results"][choice]["port"]
        print(selected_proxy_ip)
        return selected_proxy_ip, selected_proxy_port

    def confirm_public_ip(self, proxy_dict, desired_ip):

        print(proxy_dict, desired_ip, "21rm")
        r, r2 = ProxyAPI().get_public_ip(proxy_dict)
        print(desired_ip, r.text, r2.text, "23rm")
        ip_is_correct = r.text == desired_ip and r2.text == desired_ip
        return ip_is_correct



class ProxyAPI:
    def __init__(self):
        pass

    def get_proxy_connection_info(self, token):
        download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"
        return requests.get(download_list, headers={"Authorization": "Token " + token})

    def get_public_ip(self, proxy_dict):
        print(requests, proxy_dict, "43rm")
        api_key = os.environ.get("apikey")
        headers = {"Authorization": "Token " + api_key}
        print(headers)
        r = requests.get('https://api.ipify.org', headers=headers, proxies=proxy_dict)  # OK
        r2 = requests.get('https://api.my-ip.io/ip', headers=headers, proxies=proxy_dict)  # OK
        return r, r2


proxy_ip_and_port = ProxyTools().get_proxy_ip(0)
proxy_dict = ProxyTools().create_proxy_dict(proxy_ip_and_port[0], proxy_ip_and_port[1])
is_correct = ProxyTools().confirm_public_ip(proxy_dict, proxy_ip_and_port[0])
