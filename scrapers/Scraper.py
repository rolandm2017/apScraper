from ..util.proxyTools import ProxyTools
from .Provider import Provider
from .QueryString import QueryString
from .MapBoundaries import MapBoundaries
from ..api.websitesAPI import WebsitesAPI
from ..api.internalAPI import InternalAPI
from ..scrapers.Task import Task


class Scraper:
    def __init__(self, source):
        self.provider = source
        self.proxy_dict = None
        self.results = None
        self.queue = None

    def refresh_proxy(self):
        proxy_ip, proxy_port = ProxyTools().get_proxy_ip(0)
        # http_proxy_string = "http://" + str(proxy_ip) + ":" + str(proxy_port)
        # # https_proxy_string = "https://" + str(proxy_ip) + ":" + str(proxy_port)
        # proxy = {"http": http_proxy_string, "https": http_proxy_string}
        proxy_dict = ProxyTools().create_proxy_dict(proxy_ip, proxy_port)
        public_ip_is_correct = ProxyTools().confirm_public_ip(proxy_dict, proxy_ip)
        if public_ip_is_correct:
            self.proxy_dict = proxy_dict
        else:
            print(public_ip_is_correct, proxy_ip)
            # TODO: if proxy ip isn't set, retry setting it <= 5x
            raise NotImplementedError("The expected proxy IP was different from public IP")

    def ask_for_tasks(self):
        task_details = InternalAPI(self.provider).ask_for_tasks()
        tasks = []
        for d in task_details:
            task = Task(d["id"], d["lat"], d["long"], d["zoomWidth"])
            tasks.append(task)
        return tasks

    def accept_task(self, task):
        self.scrape(task)

    def get_results(self):
        return self.results
    
    def report_apartments(self, results):
        report_was_successful = InternalAPI().report_findings(results)
        return report_was_successful

    def scrape(self, task):
        if self.provider.type == Provider.rentCanada:
            return self.scrape_rent_canada(task)
        elif self.provider.type == Provider.rentFaster:
            return self.scrape_rent_faster(task)
        elif self.provider.type == Provider.rentSeeker:
            return self.scrape_rent_seeker(task)
        else:
            print(self.provider)
            raise ValueError("invalid scraper type")

    def scrape_rent_canada(self, task):
        """
            Uses lat and long to query RentCanada.com for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.
            NOTE: In RentCanada's coordinate system, West is negative, East is positive.
            :return: A list of apartments.
            """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method

        lat = task.lat  # was task["lat"]
        long = task.long  # task["long"]

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)
        # print(bounds, "70rm")
        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        # print(start, "72rm")
        # No map boundaries needed here apparently
        results = WebsitesAPI(self.provider).scrape_rent_canada(start, self.proxy_dict)
        # print(text.count("propertyId"))
        # print(lat, long, len(results))
        # print(results, "75rm")
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

    def add_failure_to_logs(self, failure_details):
        # todo: will do this later
        pass

    def report_failure_for(self, task):
        # todo: will do this later
        pass

