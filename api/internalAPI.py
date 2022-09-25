import requests
import os
from dotenv import load_dotenv

load_dotenv()

task_queue_address = os.environ.get("task_queue_address")


class InternalAPI:
    def __init__(self, source):
        self.provider = source
        pass

    def ask_for_task(self):
        payload = {"provider": self.provider.type}
        print(task_queue_address + "/next_task_for_scraper")
        r = requests.get(task_queue_address + "/next_task_for_scraper", json=payload)
        print(r.text)
        if r.status_code == 200:
            return r.json()
        else:
            raise NotImplementedError("No response from taskQueue")

    def report_findings(self, apartments):
        payload = {"provider": self.provider.type, "apartments": apartments}
        r = requests.post(task_queue_address + "/report_findings", json=payload)
        return r.status_code == 200

    def mark_task_complete(self, task_id):
        payload = {"provider": self.provider.type, "taskId": task_id}
        r = requests.post(task_queue_address + "/mark_task_complete", json=payload)
        return r.status_code == 200
