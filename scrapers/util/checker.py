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
    r2 = s.get('https://api.my-ip.io/ip', proxies=proxyDict) # OK
    result = r.text
    result2 = r2.text
    return result, result2