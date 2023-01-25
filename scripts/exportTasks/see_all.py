import requests
import json

url = "http://127.0.0.1:8000/task-queue/all"

r = requests.get(url)
results = r.json()["tasks"]

file_name = "tasks.ts"
print(len(results))
newline = "\n"
json_string = newline + newline + "export const massiveTasksFile: " + json.dumps(results)
with open(file_name, "w") as f:
    f.write(json_string)
