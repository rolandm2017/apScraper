from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth


load_dotenv()

token = os.environ.get("api-token")
print(token)

download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"


def get_proxy_ip(choice):
    r = requests.get(download_list, headers={"Authorization": "Token " + token})
    selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
    selected_proxy_port = r.json()["results"][choice]["port"]
    print(selected_proxy_ip)
    return selected_proxy_ip, selected_proxy_port

proxy_ip = "170.81.35.26"
proxy_port = "36681"
# proxy_ip, proxy_port = get_proxy_ip(0)
http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
# proxy = {"http": http_proxy_string, "https": https_proxy_string}
proxy = {"https": https_proxy_string}

s = requests.Session()
# proxy = {"http": proxy_string}
s.proxies.update(proxy)
# r = s.get("https://api.ipify.org", proxies={"http": proxy_string})
r = s.get("https://api.ipify.org")
result = r.text
print(result)