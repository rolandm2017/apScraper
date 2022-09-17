import requests

class ProxyAPI:
    def __init__(self):
        pass

    def get_proxy_connection_info(self, token):
        download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"
        return requests.get(download_list, headers={"Authorization": "Token " + token})
