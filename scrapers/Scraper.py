from proxyTools.ipgetter import get_proxy_ip
from proxyTools.checker import confirm_public_ip
from .Provider import Provider
from .QueryString import QueryString
from .MapBoundaries import MapBoundaries
from api import WebsitesAPI


class Scraper:
    def __init__(self, source):
        self.provider = source
        self.proxy_dict = None
        self.results = None

    def refresh_proxy(self):
        proxy_ip, proxy_port = get_proxy_ip(0)
        http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
        https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        proxy = {"http": http_proxy_string, "https": https_proxy_string}
        public_ip_is_correct = confirm_public_ip(proxy, proxy_ip)
        if public_ip_is_correct:
            self.proxy_dict = proxy
        else:
            print(public_ip_is_correct, proxy_ip)
            # TODO: if proxy ip isn't set, retry setting it <= 5x
            raise NotImplementedError("The expected proxy IP was different from public IP")

    def accept_task(self, task):
        self.scrape(task)

    def get_results(self):
        return self.results

    def scrape(self, task):
        if self.provider == Provider.rentCanada:
            return self.scrape_rent_canada(task)
        elif self.provider == Provider.rentFaster:
            return self.scrape_rent_faster(task)
        elif self.provider == Provider.rentSeeker:
            return self.scrape_rent_seeker(task)
        else:
            raise ValueError("invalid scraper type")

    def scrape_rent_canada(self, task):
        """
            Uses lat and long to query RentCanada.com for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.
            NOTE: In RentCanada's coordinate system, West is negative, East is positive.
            :return: A list of apartments.
            """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method

        lat = task["lat"]
        long = task["long"]

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)

        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        # No map boundaries needed here apparently
        results = WebsitesAPI(self.provider).scrape_rent_canada(start, self.proxy_dict)
        # print(text.count("propertyId"))
        print(lat, long, len(results))
        self.results = results
        return results

    def scrape_rent_faster(self, task):
        """
            Uses lat and long to query RentFaster.ca for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.

            :return: A list of apartments.
            """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method
        lat = task["lat"]
        long = task["long"]

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)

        start = "https://www.rentfaster.ca/api/map.json"
        raw_text_body = MapBoundaries(self.provider).add_map_boundaries(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        results = WebsitesAPI(self.provider).scrape_rent_faster(start, self.proxy_dict, raw_text_body)
        print(lat, long, len(results))
        self.results = results
        return results

    def scrape_rent_seeker(self, task):
        """
        Uses lat and long to query RentCanada.com for apartments.
        Translation from city,state,country to lat and long must be done prior to this step.

        :return: A list of apartments.
        """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method
        lat = task["lat"]
        long = task["long"]

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)

        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        raw_json_body = MapBoundaries(self.provider).add_map_boundaries(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        results = WebsitesAPI(self.provider).scrape_rent_seeker(start, self.proxy_dict, raw_json_body)
        print(lat, long, len(results))
        self.results = results
        return results