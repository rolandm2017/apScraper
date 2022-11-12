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
            print(proxy, "12rm")
            s.proxies.update(proxy)
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }

        r = s.get(start, headers=headers)
        results = r.json()
        # print(results, "18rm")
        return results

    @staticmethod
    def scrape_rent_faster(start, proxy, map_boundary_info, use_proxy=True):
        if use_proxy is True and proxy is None:
            raise ValueError("No proxy supplied")
        s = requests.Session()
        s.proxies.update(proxy)
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Cookie': 'PHPSESSID=2060b3eb3fe6ed290dcb19f3543741ec; _gcl_au=1.1.1167754990.1656991721; _ga=GA1.2.1983608871.1656991721; _gid=GA1.2.926434949.1656991721; _fbp=fb.1.1656991720812.932904256; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; lastcity=qc%2Fmontreal; _gat_UA-226906-1=1; _tac=false~google|not-available; _tas=jwhs0t4osgq'
        }
        # TODO: Update cookie occasionally
        # cookie2 = 'PHPSESSID=7185b866aede45c4c76dde286033f60a; _gcl_au=1.1.1499582163.1659423039; _ga=GA1.2.727073008.1659423039; _gid=GA1.2.1767852712.1659423039; _gat_UA-226906-1=1; _fbp=fb.1.1659423038865.1488717403; _tac=false~self|not-available; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; _tas=rrnc9ie7jv8; lastcity=qc%2Fmontreal'

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
        print(start, "51rm")
        print(map_boundary_info, "52rm")
        r = s.post(start, headers=headers, data=dumps(map_boundary_info))  # its POST in this one
        print(r.json(), '53rm')
        results = r.json()
        return results
