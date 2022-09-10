from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

def check_public_ip(proxy_dict):
    r = requests.get('https://api.ipify.org', proxies=proxy_dict) # OK
    r2 = requests.get('https://api.my-ip.io/ip', proxies=proxy_dict) # OK
    print(r.text, r2.text)

    return r.text, r2.text

    # r = s.get("https://api.ipify.org", headers={"Authorization": "Token " + token})
    # r2 = s.get('https://api.my-ip.io/ip', headers={"Authorization": "Token " + token})
    # result = r.text
    # result2 = r2.text
    # return result, result2