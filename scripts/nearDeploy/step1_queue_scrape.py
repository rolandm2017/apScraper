import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))

BATCH_NUM = 1
ZOOM_WIDTH = 13

viewport_width_url = "http://127.0.0.1:8000/housing/viewport_width"
plan_grid_url = "http://127.0.0.1:8000/task-queue/plan-grid-scan"
queue_grid_scan_url = "http://127.0.0.1:8000/task-queue/queue-grid-scan"


email = os.getenv("ADMIN_EMAIL")
password = os.getenv("ADMIN_PASSWORD")

if email is None:
    raise ValueError("Was expecting an email")
if password is None:
    raise ValueError("Was expecting a password")

admin_credentials = {
    "email": email,
    "password": password
}

providers = ["rentCanada", "rentFaster", "rentSeeker"]


class Provider:
    def __init__(self, name):
        self.name = name
        self.info = None

    def set_viewport_info(self, info):
        self.info = info

    def get_viewport_info(self):
        if self.info is not None:
            return self.info
        else:
            raise ValueError("info was none")


class Payload:
    def __init__(self, city, state, center_lat, center_long):
        self.cityName = city
        self.state = state
        self.provider = None
        self.long = center_long
        self.lat = center_lat
        self.bounds = None
        self.batch_num = None
        self.grid = None
        self.radius = 24  # just what it said in Postman

    def add_center(self, lat, long):
        self.long = long
        self.lat = lat
        return self

    def get_coords(self):
        return self.lat, self.long

    def set_provider(self, source):
        self.provider = source

    def store_bounds(self, bounds):
        self.bounds = bounds

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        if self.grid is not None:
            return self.grid
        else:
            raise ValueError("grid was none")

    def to_dict(self):
        return vars(self)


def payload_maker(city, state, source):
    return {
        "city": city, "state": state, "provider": source
    }


payloads = [
    Payload("Vancouver", "British Columbia", 49.2827, -123.1207),  # 1
    Payload("Calgary", "Alberta", 51.0447, -114.0719),  # 2
    Payload("Edmonton", "Alberta", 53.5461, -113.4937),  # 3
    Payload("Winnipeg", "Manitoba", 49.8954, -97.1385),  # 4
    Payload("Toronto", "Ontario", 43.6532, -79.3832),  # 5
    Payload("Mississauga", "Ontario", 43.589, -79.6441),  # 6
    Payload("Brampton", "Ontario", 43.7315, -79.7624),  # 7
    Payload("Hamilton", "Ontario", 43.2557, -79.8711),  # 8
    Payload("Ottawa", "Ontario", 45.4215, -75.6972),  # 9
    Payload("Montreal", "Quebec", 49.2827, -123.1207),  # 10
]

print(payloads, '77rm')
[print(x) for x in payloads]

rent_canada_payloads = [x.set_provider("rentCanada") for x in payloads]
rent_faster_payloads = [x.set_provider("rentFaster") for x in payloads]
rent_seeker_payloads = [x.set_provider("rentSeeker") for x in payloads]


current_day = datetime.now().day
current_month = datetime.now().month

flat_list = []
for sublist in [rent_canada_payloads[0:3], rent_faster_payloads[0:3], rent_seeker_payloads[0:3]]:
    for item in sublist:
        flat_list.append(item)

plan_grid_payloads = [

]


def get_viewport_width(city_name, state, provider_name):
    # city, state, provider for payload
    get_viewport_payload = {"city": city_name, "state": state, "provider": provider_name}
    viewport_width_response = requests.post(viewport_width_url, data=get_viewport_payload)
    details = viewport_width_response.json()
    return details


for provider in providers:
    viewport_details = get_viewport_width(payloads[0].cityName, payloads[0].state, provider.name)

    plan_grid_payloads.append(payload)
    # save viewport info for next time
    # filename = "viewport_dimensions_" + payload["provider"] + "_" + current_day + "_" + current_month + ".txt"
    # with open(filename, "w") as f:
    #     json = response.json()
    #     f.write(json)

queue_scans_payloads = []

for plan_grid_payload in plan_grid_payloads:
    payload_dict = plan_grid_payload.to_plan_grid_payload()
    # make the request
    response = requests.post(plan_grid_url, data=payload_dict)
    # store the response
    useful_stuff = response.json()
    plan_grid_payload.add_grid_coords(useful_stuff["gridCoords"])
    queue_scans_payloads.append(plan_grid_payload)


for queue_scan_payload in queue_scans_payloads:
    payload_dict = queue_scan_payload.to_queue_grid_scan_payload()
    # make the request
    response = requests.post(queue_grid_scan_url, data=payload_dict)
    # output some useful info
    queued = response.json()["queued"]
    output_string = f"Queued: {queued['pass']}, failed: {queued['fail']} for {payload_dict['cityName']} with {payload_dict['provider']}"
    print(output_string)
