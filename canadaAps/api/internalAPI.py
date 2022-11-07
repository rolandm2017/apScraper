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
        print(task_queue_address + "/next_tasks_for_scraper")
        r = requests.get(task_queue_address + "/next_tasks_for_scraper", json=payload)
        print(r.json(), r.status_code, self.provider.type)
        if r.status_code == 200:
            return r.json()
        else:
            raise NotImplementedError("No response from taskQueue")

    def report_findings(self, apartments):
        print(apartments, "26rm")
        payload = {"provider": self.provider.type, "apartments": apartments}
        r = requests.post(task_queue_address + "/report_findings", json=payload)
        return r.status_code == 200

    def mark_task_complete(self, task_id):
        payload = {"provider": self.provider.type, "taskId": task_id}
        r = requests.post(task_queue_address + "/mark_task_complete", json=payload)
        return r.status_code == 200
