from api.internalAPI import InternalAPI


class Task:
    def __init__(self, identifier, lat, long, viewport_width="default"):
        self.identifier = identifier
        self.lat = lat
        self.long = long
        self.viewport_width = viewport_width

    def forward_task_to_scraper(self, scraper):
        scraper.accept_task(self)

    # def report_findings(self, apartments):
    #     report_was_successful = InternalAPI().report_findings(apartments)
    #     return report_was_successful

    def mark_complete(self):
        # tell the TaskQueue to mark it complete.
        successfully_marked_complete = InternalAPI().mark_task_complete(self.identifier)
        return successfully_marked_complete
