from canadaAps.util.proxyTools import ProxyTools
from .Provider import Provider
from .QueryString import QueryString
from .MapBoundaries import MapBoundaries
from .Scrape import Scrape

from canadaAps.scraper.Task import Task


class Scraper:
    def __init__(self, source, internal_api, web_api):
        self.provider = source
        self.proxy_dict = None
        # self.results = None
        self.queue = None
        self.internal_api = internal_api
        self.web_api = web_api
        self.issue_logs = []
        self.proxy_tools = ProxyTools()

    def refresh_proxy(self):
        if self.proxy_dict:
            return  # no need to store it multiple times. also no need to request an ip from proxy service repeatedly
        proxy_ip, proxy_port = self.proxy_tools.get_proxy_ip(0)
        proxy_dict = ProxyTools().create_proxy_dict(proxy_ip, proxy_port)
        # ###
        # ##
        # Disabled because the "confirm public ip is proxy ip" api was 429ing me
        # public_ip_is_correct = self.proxy_tools.confirm_public_ip_is_proxy_ip(proxy_dict, proxy_ip)
        # ##
        # ###
        self.proxy_dict = proxy_dict
        # if public_ip_is_correct:
        #     self.proxy_dict = proxy_dict
        # else:
        #     print(proxy_dict, public_ip_is_correct, proxy_ip)
        #     # TODO: if proxy ip isn't set, retry setting it <= 5x
        #     raise NotImplementedError("The expected proxy IP was different from public IP")

    def ask_for_tasks(self):
        task_details = self.internal_api.ask_for_tasks()
        tasks = []
        for d in task_details:
            print(task_details, "42rm")
            print(d, "42rm")
            task = Task(d["taskId"], d["lat"], d["long"], d["zoomWidth"])
            tasks.append(task)
        return tasks

    def accept_task(self, task):
        self.scrape(task)
    #
    # def get_results(self):
    #     return self.results

    def report_apartments_and_mark_complete(self, task, scrape):
        report_was_successful = self.internal_api.report_findings_and_mark_complete(task, scrape.get_results())
        return report_was_successful

    def add_failure_to_logs(self, scrape):
        self.issue_logs.append(scrape)

    def report_failure_for(self, task):
        self.internal_api.report_failure_for(task, self.issue_logs)

    def reset_logs(self):
        self.issue_logs = []

    def scrape(self, task):
        if self.provider.get_type() == Provider.rentCanada:
            return self.scrape_rent_canada(task)
        elif self.provider.get_type() == Provider.rentFaster:
            return self.scrape_rent_faster(task)
        elif self.provider.get_type() == Provider.rentSeeker:
            return self.scrape_rent_seeker(task)
        else:
            print(self.provider, "77rm")
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
        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        # No map boundaries needed here apparently
        # print(lat, long, bounds, start, self.proxy_dict, "78rm")
        results = self.web_api.scrape_rent_canada(start, self.proxy_dict)
        results = Scrape(results, True)
        return results

    def scrape_rent_faster(self, task):
        """
            Uses lat and long to query RentFaster.ca for apartments.
            Translation from city,state,country to lat and long must be done prior to this step.

            :return: A list of apartments.
            """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method
        lat = task.lat
        long = task.long

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)

        start = "https://www.rentfaster.ca/api/map.json"
        raw_text_body = MapBoundaries(self.provider).add_map_boundaries(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        results = self.web_api.scrape_rent_faster(start, self.proxy_dict, raw_text_body)
        results = Scrape(results, True)
        return results

    def scrape_rent_seeker(self, task):
        """
        Uses lat and long to query RentCanada.com for apartments.
        Translation from city,state,country to lat and long must be done prior to this step.

        :return: A list of apartments.
        """
        # Note: Used to have "location = request.json" but that'll have to live *outside* of this method
        lat = task.lat
        long = task.long

        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)

        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        raw_json_body = MapBoundaries(self.provider).add_map_boundaries(bounds["north"], bounds["west"], bounds["south"], bounds["east"])

        results = self.web_api.scrape_rent_seeker(start, self.proxy_dict, raw_json_body)
        results = Scrape(results, True)
        return results
