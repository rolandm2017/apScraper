from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.environ.get("apikey")
print(token)

download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"


def get_proxy_ip(choice):
    token = os.environ.get("apikey")
    print(token)
    r = requests.get(download_list, headers={"Authorization": "Token " + token})
    selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
    selected_proxy_port = r.json()["results"][choice]["port"]
    print(selected_proxy_ip)
    return selected_proxy_ip, selected_proxy_port