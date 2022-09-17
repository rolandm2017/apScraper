import requests

class IPTestAPI:
    def __init__(self):
        pass

    def get_public_ip(self, proxy_dict):
        r = requests.get('https://api.ipify.org', proxies=proxy_dict)  # OK
        r2 = requests.get('https://api.my-ip.io/ip', proxies=proxy_dict)  # OK
        return r, r2