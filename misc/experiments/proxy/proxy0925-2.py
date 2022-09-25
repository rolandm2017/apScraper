import os
from dotenv import load_dotenv
import requests

load_dotenv()

username = os.environ.get("username2")
password = os.environ.get("password2")
token = os.environ.get("apikey")


r = requests.get("https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25", headers={"Authorization": f"Token {token}"})
# print(r.text)
proxy_ip = r.json()['results'][0]["proxy_address"]
proxy_port = r.json()['results'][0]["port"]
print(r.json()['results'][0])
print(proxy_ip,proxy_port)
print("====================================9999-=======")
proxy_string = f"http://{username}:{password}@{proxy_ip}:{proxy_port}"

proxy_test_without_username_password = f"http://{proxy_ip}:{proxy_port}"
headers = {"Authorization": "Token " + token}
proxyDict = {"http": proxy_string, "https": proxy_string}

r = requests.get('https://api.my-ip.io/ip', headers=headers, proxies=proxyDict) # OK
print(r.text)

# works - but can i do it without username,pw, andj ust an api key?