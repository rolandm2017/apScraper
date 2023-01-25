import requests
import os
from dotenv import load_dotenv

load_dotenv()

task_queue_address = os.environ.get("task_queue_address")


class InternalAPI:
    def __init__(self, source):
        self.provider = source
        pass

    def ask_for_tasks(self):
        payload = {"provider": self.provider.type}
        print(task_queue_address + "/next-tasks-for-scraper")
        r = requests.get(task_queue_address + "/next-tasks-for-scraper", json=payload)
        print("Asking for tasks:", r.status_code, self.provider.type)
        if r.status_code == 200:
            return r.json()["tasks"]
        else:
            raise NotImplementedError("No response from taskQueue")

    def report_findings_and_mark_complete(self, task, apartments):
        payload = {"provider": self.provider.type, "taskId": task.identifier, "apartments": apartments}
        print("sending payload:")
        print(payload)
        r = requests.post(task_queue_address + "/report-findings-and-mark-complete", json=payload)
        return r.status_code == 200

    def report_failure_for(self, task, scrapes):
        payload = {
            "provider": self.provider.type,
            "task_id": task.identifier,
            "issues": [{"reason": x.issue} for x in scrapes]
        }
        r = requests.post(task_queue_address + "/report-failure", json=payload)
        return r.status_code == 200
