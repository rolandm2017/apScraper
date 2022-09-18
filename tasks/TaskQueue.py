import requests
import os

from .Task import Task
from ..api.internal import InternalAPI

class TaskQueue:
    def __init__(self, source):
        self.provider = source

    def get_all_tasks(self):
        # Don't do this
        pass

    def get_next_task(self):
        # payload = {"provider": self.provider}
        # r = requests.get(task_queue_address + "/nextTaskForScraper", json=payload)
        task_details = InternalAPI().ask_for_task(self.provider)
        task = Task(task_details["lat"], task_details["long"], task_details["zoomWidth"], self)
        return task

    def mark_task_complete(self, task):
        # payload = {"taskId": task.id}
        # r = requests.post(task_queue_address + "/markTaskComplete", json=payload)
        successfully_marked_complete = InternalAPI().mark_task_complete(task.id)
        return successfully_marked_complete

    def get_next_batch(self):
        # TBD whether this is needed
        pass
