from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

def check_public_ip(proxy):
    s = requests.Session()
    # proxy = {"http": proxy_string}
    s.proxies.update(proxy)
    # r = s.get("https://api.ipify.org", proxies={"http": proxy_string})
    r = s.get("https://api.ipify.org")
    result = r.text
    return result