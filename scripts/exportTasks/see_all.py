import requests
import json

url = "http://127.0.0.1:8000/task-queue/all"

r = requests.get(url)
results = r.json()["tasks"]

file_name = "tasks.ts"
print(len(results))
for result in results:
    del result["createdAt"]
    del result["updatedAt"]
newline = "\n"
# check how many per provider
# just_rent_canada = [x for x in results if x["providerName"] == "rentCanada"]
# just_faster =  [x for x in results if x["providerName"] == "rentFaster"]
# just_seeker =  [x for x in results if x["providerName"] == "rentSeeker"]
# print(len(just_rent_canada), len(just_faster), len(just_seeker))
json_string = newline + newline + "export const SEED_TASKS: TaskCreationAttributes[]  = " + json.dumps(results)
with open(file_name, "w") as f:
    f.write('import { TaskCreationAttributes } from "../database/models/Task";')
    f.write("\n\n")
    f.write(json_string)
