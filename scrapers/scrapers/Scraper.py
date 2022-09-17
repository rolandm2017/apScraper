import requests

from ..proxyTools.ipgetter import get_proxy_ip
from ..proxyTools.checker import confirm_public_ip
from .QueryString import QueryString
from .MapBoundaries import MapBoundaries
from ..api.internal import InternalAPI
from ..api.websites import WebsitesAPI
from ..api.ipTest import IPTestAPI

class Scraper:
    def __init__(self, source):
        self.provider = source
        self.current_task = None

    def accept_task(self, task):
        self.current_task = task
        self.scrape(task)

    def scrape(self, task):
        if self.provider == "rentCanada":
            return self.scrape_rent_canada(task)
        elif self.provider == "rentFaster":
            return self.scrape_rent_faster(task)
        elif self.provider == "rentSeeker":
            return self.scrape_rent_seeker(task)
        else:
            raise ValueError("invalid scraper type")

    def scrape_rent_canada(self, task):
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
        public_ip_is_correct = confirm_public_ip(proxy, proxy_ip)
        if public_ip_is_correct:
            pass
        else:
            print(public_ip_is_correct, proxy_ip)
            # TODO: if proxy ip isn't set, retry setting it <= 5x
            raise NotImplementedError("The expected proxy IP was different from public IP")

        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method

        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = task["lat"]
        long = task["long"]

        lat_padding = 0.053241287376788904
        long_padding = 0.04231452941894531

        lat_bound_up = lat + lat_padding  # calculated in the distance.py file
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = QueryString(self.provider).make_query_string(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)
        # No map boundaries needed here apparently
        results = WebsitesAPI(self.provider).scrape_rent_canada(start, proxy)
        # print(text.count("propertyId"))
        print(lat, long, len(results))
        return results

    def scrape_rent_faster(self, task):
        """
            Uses lat and long to query RentFaster.ca for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.

            :return: A list of gyms.
            """

        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method

        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = task["lat"]
        long = task["long"]

        lat_padding = 0.0978503023843551  # calculated in the distance.py file
        long_padding = 0.09698867797851562

        lat_bound_up = lat + lat_padding
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = "https://www.rentfaster.ca/api/map.json"
        raw_text_body = MapBoundaries(self.provider).add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)
        results = WebsitesAPI(self.provider).scrape_rent_faster(start, proxy, raw_text_body)
        print(lat, long, len(results))
        return results

    def scrape_rent_seeker(self, task):
        """
        Uses lat and long to query RentCanada.com for apartments.
        Translation from city,state,country to lat and long must be done prior to this step.

        :return: A list of gyms.
        """

        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method

        # city = location["city"]
        # state = location["state"]
        # country = location["country"]
        lat = task["lat"]
        long = task["long"]

        lat_padding = 0.0978503023843551  # calculated in the distance.py file
        long_padding = 0.09698867797851562

        lat_bound_up = lat + lat_padding
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding

        start = QueryString(self.provider).make_query_string(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)
        raw_json_body = MapBoundaries(self.provider).add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)
        results = WebsitesAPI(self.provider).scrape_rent_seeker(start, proxy, raw_json_body)
        print(lat, long, len(results))
        return results