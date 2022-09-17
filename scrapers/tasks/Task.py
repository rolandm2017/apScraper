from ..api.internal import InternalAPI

class Task:
    def __init__(self, lat, long, viewport_width, queue):
        # not convinced this needs to be here, since the TaskQueue has it & the entire instance will be set to it
        self.lat = lat
        self.long = long
        self.viewport_width = viewport_width
        self.queue = queue
        self.is_ready = True

    def forward_task_to_scraper(self, scraper):
        scraper.accept_task(self)

    def report_findings(self, apartments):
        report_was_successful = InternalAPI().report_findings(apartments)
        return report_was_successful

    def mark_complete(self):
        # tell the TaskQueue to mark it complete.
        self.queue.mark_complete()
