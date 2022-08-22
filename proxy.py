from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPProxyAuth

load_dotenv()

token = os.environ.get("api-token")


requests.get("https://proxy.webshare.io/api/v2/profile/", headers={"Authorization": "Token <TOKEN>"})
