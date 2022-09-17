import requests

apartment_findings_reporting_url = "placeholder"

class Task:
    def __init__(self, provider, lat, long, viewport_width, queue):
        # not convinced this needs to be here, since the TaskQueue has it & the entire instance will be set to it
        self.provider = provider
        self.lat = lat
        self.long = long
        self.viewport_width = viewport_width
        self.queue = queue

    def forward_task_to_scraper(self, scraper):
        scraper.accept_task(self)

    def report_findings(self, apartments):
        payload = {"apartments": apartments}
        r = requests.post(apartment_findings_reporting_url, json=payload)
        return r.status_code == 200

    def mark_complete(self):
        # tell the TaskQueue to mark it complete.
        self.queue.mark_complete()
