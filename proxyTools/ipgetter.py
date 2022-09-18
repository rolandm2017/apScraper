# from dotenv import load_dotenv
import os

from ..api.proxy import ProxyAPI

# load_dotenv()

token = os.environ.get("apikey")
print(token)

def get_proxy_ip(choice):
    token = os.environ.get("apikey")
    r = ProxyAPI().get_proxy_connection_info(token)
    selected_proxy_ip = r.json()["results"][choice]["proxy_address"]
    selected_proxy_port = r.json()["results"][choice]["port"]
    print(selected_proxy_ip)
    return selected_proxy_ip, selected_proxy_port