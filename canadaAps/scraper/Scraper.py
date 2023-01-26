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
        successful_refresh = False
        proxy_list_choice = 0
        while not successful_refresh:
            proxy_ip, proxy_port = self.proxy_tools.get_proxy_ip(proxy_list_choice)
            if proxy_ip is None or proxy_port is None:

                print(f"Throttled! Switching from proxy {proxy_list_choice} to  {proxy_list_choice + 1}")
                proxy_list_choice = proxy_list_choice + 1
                # handle out of range (only have 0 to 9)
                if proxy_list_choice == 9:
                    proxy_list_choice = 0
            else:
                successful_refresh = True
        proxy_dict = ProxyTools().create_proxy_dict(proxy_ip, proxy_port)
        # ###
        # ##
        # Disabled because the "confirm public ip is proxy ip" api was 429ing me
        # public_ip_is_correct = self.proxy_tools.confirm_public_ip_is_proxy_ip(proxy_dict, proxy_ip)
        # ##
        # ###
        self.proxy_dict = proxy_dict

    def ask_for_tasks(self):
        task_details = self.internal_api.ask_for_tasks()
        tasks = []
        for d in task_details:
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
        print(f"getting scrape for rent canada at {long}, {lat}")
        bounds = MapBoundaries(self.provider).make_boundaries(lat, long)
        start = QueryString(self.provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
        # No map boundaries needed here apparently
        # print(lat, long, bounds, start, self.proxy_dict, "78rm")
        results = self.web_api.scrape_rent_canada(start, self.proxy_dict)
        num_of_results = len(results["listings"])
        print("\n==\n==\n--\n==\n--\n==")
        print("results:", len(results["listings"]))
        # log if results were nil
        if num_of_results == 0:
            print(f"Empty task discovered for {lat}, {long} at rentCanada")
        print("len of results:" + str(len(results["listings"])))
        results = Scrape(results, True)
        return results, num_of_results

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
        num_of_results = len(results["listings"])
        print("\n==\n==\n--\n==\n--\n==")
        print("results:", len(results["listings"]))
        if num_of_results == 0:
            print(f"Empty task discovered for {lat}, {long} at rentFaster")
        print("len of results:" + str(len(results["listings"])))
        results = Scrape(results, True)
        return results, num_of_results

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
        num_of_results = len(results["hits"])
        print("\n==\n==\n--\n==\n--\n==\n 154rm")
        print("results:", len(results["hits"]))
        if num_of_results == 0:
            print(f"Empty task discovered for {lat}, {long} at rentSeeker")
        print("len of results:" + str(len(results["hits"])))
        results = Scrape(results, True)
        return results, num_of_results

    def get_missing_url_for_id(self, missing_url_id):
        missing_url = self.web_api.get_missing_url(missing_url_id, self.proxy_dict)
        return missing_url
