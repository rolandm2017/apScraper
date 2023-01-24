import requests
import datetime
import os

BATCH_NUM = 1
ZOOM_WIDTH = 13

viewport_width_url = "http://127.0.0.1:8000/housing/viewport_width"
plan_grid_url = "http://127.0.0.1:8000/task-queue/plan-grid-scan"
queue_grid_scan_url = "http://127.0.0.1:8000/task-queue/queue-grid-scan"


email = os.environ.get("ADMIN_EMAIL")
password = os.environ.get("ADMIN_PASSWORD")

if email is None:
    raise ValueError("Was expecting an email")
if password is None:
    raise ValueError("Was expecting a password")

admin_credentials = {
    "email": email,
    "password": password
}


class Payload:
    def __init__(self, city, state):
        self.cityName = city
        self.state = state
        self.provider = None
        self.long = None
        self.lat = None
        self.bounds = None
        self.batch_num = None
        self.radius = 24  # just what it said in Postman

    def add_center(self, lat, long):
        self.long = long
        self.lat = lat

    def set_provider(self, source):
        self.provider = source

    def store_bounds(self, bounds):
        self.bounds = bounds

    def to_dict(self):
        return vars(self)


def payload_maker(city, state, source):
    return {
        "city": city, "state": state, "provider": source
    }

providers = ["rentCanada", "rentFaster", "rentSeeker"]

payloads = [
    Payload("Vancouver", "British Columbia").add_center(49.2827, -123.1207),  # 1
    Payload("Calgary", "Alberta").add_center(51.0447, -114.0719),  # 2
    Payload("Edmonton", "Alberta").add_center(53.5461, -113.4937),  # 3
    Payload("Winnipeg", "Manitoba").add_center(49.8954, -97.1385),  # 4
    Payload("Toronto", "Ontario").add_center(43.6532, -79.3832),  # 5
    Payload("Mississauga", "Ontario").add_center(43.589, -79.6441),  # 6
    Payload("Brampton", "Ontario").add_center(43.7315, -79.7624),  # 7
    Payload("Hamilton", "Ontario").add_center(43.2557, -79.8711),  # 8
    Payload("Ottawa", "Ontario").add_center(45.4215, -75.6972),  # 9
    Payload("Montreal", "Quebec").add_center(49.2827, -123.1207),  # 10
]

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


for payload in payloads[0:3]:
    payload_dict = payload.to_get_viewport_width_payload()
    response = requests.post(viewport_width_url, data=payload)
    payload.store_bounds(response.json())
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
