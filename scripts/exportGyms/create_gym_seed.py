import requests
import json

def make_loc_dict(city_name):
    return {
        "cityName": city_name,
    }


location_dicts = [
    make_loc_dict("Vancouver"),
    make_loc_dict("Calgary"),
    make_loc_dict("Edmonton"),
    make_loc_dict("Winnipeg"),
    make_loc_dict("Toronto"),
    make_loc_dict("Ottawa"),
    make_loc_dict("Mississauga"),
    make_loc_dict("Brampton"),
    make_loc_dict("Hamilton"),
    make_loc_dict("Montreal")
]

for loc in location_dicts:
    city_name = loc["cityName"]
    # url = f"http://127.0.0.1:8000/google/gyms?cityName={city_name}"
    url = f"http://127.0.0.1:8000/google/saved"
    r = requests.get(url, params={"cityName": city_name})
    results = r.json()
    # remove updatedAt and createdAt
    for result in results:
        del result["createdAt"]
        del result["updatedAt"]
    # make file
    # file_name = city_name + ".json"
    file_name = city_name + ".ts"
    print(len(results))
    importing_stuff = 'import { GymCreationAttributes } from "../../database/models/Gym";'
    newline = "\n"
    json_string = importing_stuff + newline + newline + "export const " + city_name + "= " + json.dumps(results)
    with open(file_name, "w") as f:
        f.write(json_string)
    print("saved data for " + city_name)

