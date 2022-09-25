from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

load_dotenv()

username = os.environ.get("username")
password = os.environ.get("password")
token = os.environ.get("apikey")

proxy_ip = os.environ.get("proxy1ip")
proxy_port = os.environ.get("proxy1port")

proxy2_ip = os.environ.get("proxy2ip")
proxy2_port = os.environ.get("proxy2port")

print(username, password, token)

r = requests.get("https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25", headers={"Authorization": f"Token {token}"})
# print(r.text)
proxy_ip = r.json()['results'][0]["proxy_address"]
proxy_port = r.json()['results'][0]["port"]
print(r.json()['results'][0])
print(proxy_ip,proxy_port)
print("====================================9999-=======")
proxy_string = f"http://{username}:{password}@{proxy_ip}:{proxy_port}"
proxyDict = {"http": proxy_string, "https": proxy_string}

r = requests.get('https://api.my-ip.io/ip', proxies=proxyDict) # OK
print(r.text)

proxy_string = f"http://{username}:{password}@{proxy_ip}:{proxy_port}"
proxyDict = {"http": proxy_string, "https": proxy_string}

r = requests.get('https://api.my-ip.io/ip', proxies=proxyDict) # OK
print(r.text)

# the real tests
proxy_string = f"http://{username}:{password}@{proxy_ip}:{proxy_port}"
proxyDict = {"http": proxy_string, "https": proxy_string}
r = requests.get('https://api.ipify.org', proxies=proxyDict) # OK
print(r.text)

proxy_string = f"http://{username}:{password}@{proxy_ip}:{proxy_port}"
proxyDict = {"http": proxy_string, "https": proxy_string}
r = requests.get('https://api.ipify.org', proxies=proxyDict) # OK
print(r.text)