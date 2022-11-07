import requests


class ProxyAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_connection_info(token):
        download_list = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"
        return requests.get(download_list, headers={"Authorization": "Token " + token})

    @staticmethod
    def get_public_ip(proxy_dict):
        print(proxy_dict)
        r = requests.get('http://api.ipify.org', proxies=proxy_dict)  # OK
        r2 = requests.get('http://api.my-ip.io/ip', proxies=proxy_dict)  # OK
        print(r)
        print(r2)
        return r, r2
