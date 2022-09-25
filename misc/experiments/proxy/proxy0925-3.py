from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

load_dotenv()
token = os.environ.get("apikey")
x = requests.get("https://proxy.webshare.io/api/profile/", headers={"Authorization": "Token %s" % token})

print(x.json())