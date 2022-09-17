import requests
import os

from .Task import Task

task_queue_address = "placeholder"

class TaskQueue:
    def __init__(self, source):
        self.provider = source

    def get_all_tasks(self):
        # Don't do this
        pass

    def get_next_task(self):
        payload = {"provider": self.provider}
        r = requests.get(task_queue_address + "/nextTaskForScraper", json=payload)
        task = r.json()
        task = Task(task["lat"], task["long"], task["zoomWidth"], self)
        return task

    def mark_complete(self, task):
        payload = {"taskId": task.id}
        r = requests.post(task_queue_address + "/markTaskComplete", json=payload)
        return r.status_code == 200

    def get_next_batch(self):
        # TBD whether this is needed
        pass
