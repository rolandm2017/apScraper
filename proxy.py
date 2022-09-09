from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

load_dotenv()

token = os.environ.get("api-token")
print(token)

download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"

r = requests.get(download_list, headers={"Authorization": "Token " + token})
selected_proxy_ip = r.json()["results"][0]["proxy_address"]
print(selected_proxy_ip)