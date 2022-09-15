import requests
from flask import Flask, request, make_response

from ..shared.ipgetter import get_proxy_ip
from ..shared.checker import check_public_ip

class Scrape:
    def __init__(self, source):
        self.provider = source

    def scrape(self):
        if self.provider == "rentCanada":
            return self.scrapeRentCanada()
        elif self.provider == "rentFaster":
            return self.scrapeRentFaster()
        elif self.provider == "rentSeeker":
            return self.scrapeRentSeeker()

    def scrapeRentCanada(self, lat, long):
        """
            Uses lat and long to query RentCanada.com for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.
            NOTE: In RentCanada's coordinate system, West is negative, East is positive.
            :return: A list of gyms.
            """
        proxy_ip, proxy_port = get_proxy_ip(0)
        http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
        https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy = {"http": http_proxy_string, "https": https_proxy_string}
        public_ip = check_public_ip(proxy)
        if public_ip == proxy_ip:
            pass
        else:
            print(public_ip, proxy_ip)
            raise NotImplementedError("The expected proxy IP was different from public IP")
        location = request.json
        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = location["lat"]
        long = location["long"]

        lat_padding = 0.053241287376788904
        long_padding = 0.04231452941894531

        lat_bound_up = lat + lat_padding  # calculated in the distance.py file
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = make_query_string(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

        s = requests.Session()
        s.proxies.update(proxy)
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }
        r = s.get(start, headers=headers)

        results = r.json()
        # print(text.json(), "19rm")

        # print(text.count("propertyId"))
        print(lat, long, len(results))
        return results

    def scrapeRentFaster(self):
        """
            Uses lat and long to query RentFaster.ca for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.

            :return: A list of gyms.
            """

        location = request.json
        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = location["lat"]
        long = location["long"]

        lat_padding = 0.0978503023843551  # calculated in the distance.py file
        long_padding = 0.09698867797851562

        lat_bound_up = lat + lat_padding
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = "https://www.rentfaster.ca/api/map.json"

        s = requests.Session()
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Cookie': 'PHPSESSID=2060b3eb3fe6ed290dcb19f3543741ec; _gcl_au=1.1.1167754990.1656991721; _ga=GA1.2.1983608871.1656991721; _gid=GA1.2.926434949.1656991721; _fbp=fb.1.1656991720812.932904256; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; lastcity=qc%2Fmontreal; _gat_UA-226906-1=1; _tac=false~google|not-available; _tas=jwhs0t4osgq'
        }

        cookie2 = 'PHPSESSID=7185b866aede45c4c76dde286033f60a; _gcl_au=1.1.1499582163.1659423039; _ga=GA1.2.727073008.1659423039; _gid=GA1.2.1767852712.1659423039; _gat_UA-226906-1=1; _fbp=fb.1.1659423038865.1488717403; _tac=false~self|not-available; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; _tas=rrnc9ie7jv8; lastcity=qc%2Fmontreal'

        raw_text_body = add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

        r = s.post(start, headers=headers, data=raw_text_body)  # its POST in this one

        results = r.json()
        print(lat, long, len(results))
        return results

    def scrapeRentSeeker(self):
        """
        Uses lat and long to query RentCanada.com for apartments.
        Translation from city,state,country to lat and long must be done prior to this step.

        :return: A list of gyms.
        """

        location = request.json
        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = location["lat"]
        long = location["long"]

        lat_padding = 0.0978503023843551  # calculated in the distance.py file
        long_padding = 0.09698867797851562

        lat_bound_up = lat + lat_padding
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = make_query_string()

        s = requests.Session()
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }

        # raw_JSON_body = '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=%5B%5B45.45344020494669%2C-73.65633240761402%2C45.6491408097154%2C-73.46235505165698%5D%5D"}'
        raw_json_body = add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

        r = s.post(start, headers=headers, data=raw_json_body)  # its POST in this one

        results = r.json()
        print(lat, long, len(results))
        return results