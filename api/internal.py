import requests

apartment_findings_reporting_url = "placeholder"

task_queue_address = "placeholder"

class InternalAPI:
    def __init__(self):
        pass

    def ask_for_task(self, provider):
        payload = {"provider": provider}
        r = requests.get(task_queue_address + "/nextTaskForScraper", json=payload)
        if r.status_code == 200:
            return r.json()
        else:
            return False

    def report_findings(self, apartments):
        payload = {"apartments": apartments}
        r = requests.post(apartment_findings_reporting_url, json=payload)
        return r.status_code == 200

    def mark_task_complete(self, task_id):
        payload = {"taskId": task_id}
        r = requests.post(task_queue_address + "/markTaskComplete", json=payload)
        return r.status_code == 200