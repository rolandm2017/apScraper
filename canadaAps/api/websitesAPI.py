import requests
from json import dumps

class WebsitesAPI:
    def __init__(self):
        pass

    @staticmethod
    def scrape_rent_canada(start, proxy, use_proxy=True):
        if use_proxy is True and proxy is None:
            raise ValueError("No proxy supplied")
        s = requests.Session()
        if use_proxy:
            s.proxies.update(proxy)
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }

        r = s.get(start, headers=headers)
        results = r.json()
        return results

    @staticmethod
    def scrape_rent_faster(start, proxy, map_boundary_info, use_proxy=True):
        if use_proxy is True and proxy is None:
            raise ValueError("No proxy supplied")
        s = requests.Session()
        s.proxies.update(proxy)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded', # crucial.
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Cookie': 'PHPSESSID=2060b3eb3fe6ed290dcb19f3543741ec; _gcl_au=1.1.1167754990.1656991721; _ga=GA1.2.1983608871.1656991721; _gid=GA1.2.926434949.1656991721; _fbp=fb.1.1656991720812.932904256; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; lastcity=qc%2Fmontreal; _gat_UA-226906-1=1; _tac=false~google|not-available; _tas=jwhs0t4osgq'
        }
        # todo: could the cookie be out of date?
        r = s.post(start, headers=headers, data=map_boundary_info)  # its POST in this one
        results = r.json()
        return results

    @staticmethod
    def scrape_rent_seeker(start, proxy, map_boundary_info, use_proxy=True):
        if use_proxy is True and proxy is None:
            raise ValueError("No proxy supplied")
        s = requests.Session()
        s.proxies.update(proxy)
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }
        r = s.post(start, headers=headers, data=dumps(map_boundary_info))  # its POST in this one
        results = r.json()
        return results

    @staticmethod
    def get_missing_url(missing_url_id, proxy):
        s = requests.Session()
        s.proxies.update(proxy)
        response = s.get("https://www.rentcanada.com/api/listing/" + missing_url_id)
        data = response.json()
        print(data, '60rm')
        url = data["listing"]["url"]
        print(url)
        return url
