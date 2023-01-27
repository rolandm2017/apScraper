import requests
from datetime import datetime
import os
from dotenv import load_dotenv

from classes import Provider, City, Payload

load_dotenv()

print(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))

BATCH_NUM = 2
ZOOM_WIDTH = 13

login_url = "http://127.0.0.1:8000/auth/authenticate"
ref_token_url = "http://127.0.0.1:8000/auth/refresh-token"
viewport_width_url = "http://127.0.0.1:8000/housing/viewport-width"
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


def get_ref_token(credentials):
    # returns ref token
    r = requests.post(login_url, json=credentials)
    refresh_token = r.cookies.get_dict()
    return refresh_token


def trade_ref_token_for_jwt(ref_token_cookie):
    response = requests.post(ref_token_url, cookies=ref_token_cookie)
    response_details = response.json()
    role = response_details["role"]
    if role != "ADMIN":
        raise ValueError("Did not get an admin account")
    jwt = response_details["jwtToken"]
    return jwt


def get_admin_jwt(credentials):
    ref_token = get_ref_token(credentials)
    jwt = trade_ref_token_for_jwt(ref_token)
    return jwt


# login get admin jwt
admin_jwt = get_admin_jwt(admin_credentials)
print("admin jwt:", admin_jwt)

providers = [Provider("rentCanada", 5)]
# providers = [Provider("rentCanada", 4), Provider("rentFaster", 4), Provider("rentSeeker", 4)]


cities = [
    City("Vancouver", "British Columbia", 49.2827, -123.1207),  # 1
    City("Calgary", "Alberta", 51.0447, -114.0719),  # 2
    City("Edmonton", "Alberta", 53.5461, -113.4937),  # 3
    City("Winnipeg", "Manitoba", 49.8954, -97.1385),  # 4
    City("Toronto", "Ontario", 43.6532, -79.3832),  # 5
    City("Mississauga", "Ontario", 43.589, -79.6441),  # 6
    City("Brampton", "Ontario", 43.7315, -79.7624),  # 7
    City("Hamilton", "Ontario", 43.2557, -79.8711),  # 8
    City("Ottawa", "Ontario", 45.4215, -75.6972),  # 9
    City("Montreal", "Quebec", 45.5019, -73.5674),  # 10
]


rent_canada_viewport_details = None
rent_faster_viewport_details = None
rent_seeker_viewport_details = None

# rent_canada_payloads = [x.set_provider("rentCanada") for x in cities]
# rent_faster_payloads = [x.set_provider("rentFaster") for x in cities]
# rent_seeker_payloads = [x.set_provider("rentSeeker") for x in cities]


def get_bounds_for(provider_name):
    if provider_name == "rentCanada":
        return rent_canada_viewport_details
    elif provider_name == "rentFaster":
        return rent_faster_viewport_details
    elif provider_name == "rentSeeker":
        return rent_seeker_viewport_details
    else:
        raise ValueError("Unexpected provider")

def get_viewport_width(city_name, state, provider_name, viewport_width):
    # city, state, provider for payload
    get_viewport_payload = {"city": city_name, "state": state, "provider": provider_name, "zoomWidth": viewport_width}
    viewport_width_response = requests.post(viewport_width_url, data=get_viewport_payload)
    status = viewport_width_response.status_code
    print(viewport_width_response, '31rm')
    details = viewport_width_response.json()
    print(details, '33rm')
    return details


def get_grid_plan(start_coords, bounds, radius):
    payload = {"startCoords": start_coords, "bounds": bounds, "radius": radius}
    r = requests.post(plan_grid_url, json=payload, headers={"Authorization": "Bearer " + admin_jwt})
    if r.status_code != 200:
        print("r status code:", r.status_code, r)
        raise ValueError("Expected 200 status code")
    grid_response = r.json()
    return grid_response


def queue_grid_scan(payload):
    # print(payload, '122rm')
    response = requests.post(queue_grid_scan_url, json=payload, headers={"Authorization": "Bearer " + admin_jwt})
    if response.status_code != 200:
        print(response.status_code, 'failure :: 124rm')
        return 0
    queued_details = response.json()
    print("queue details:")
    print(queued_details)
    return queued_details["queued"]


canada_grid_payloads = []
faster_grid_payloads = []
seeker_grid_payloads = []


base_city = City("Montreal", "Quebec", 49.2827, -123.1207)  # 10

print(base_city.name, '36rm')
# providers = [Provider("rentFaster"), Provider("rentSeeker")]

# step 1: get the viewport width and store it
rent_canada_viewport_details = get_viewport_width(base_city.name, base_city.state, "rentCanada", 5)
rent_faster_viewport_details = get_viewport_width(base_city.name, base_city.state, "rentFaster", 5)
rent_seeker_viewport_details = get_viewport_width(base_city.name, base_city.state, "rentSeeker", 5)
# rent_canada_viewport_details = {
#     'north': 45.5521275,
#     'east': -73.5389464,
#     'south': 45.4509234,
#     'west': -73.6094939,
#     'latitudeChange': 0.1012040999999968,
#     'longitudeChange': 0.07054750000000354,
#     'kmNorthSouth': 3.175507162201125,
#     'kmEastWest': 7.8445240874574
# }
# rent_faster_viewport_details = {
#     'north': 47.15,
#     'east': -72.283333,
#     'south': 45.4269725,
#     'west': -73.8954914,
#     'latitudeChange': 1.7230275000000006,
#     'longitudeChange': 1.6121583999999984,
#     'kmNorthSouth': 53.14388225926579,
#     'kmEastWest': 179.26383502740902
# }
#
# rent_seeker_viewport_details = {
#     'north': '45.5816140',
#     'east': '-73.6617082',
#     'south': '45.4487298',
#     'west': '-73.4725306',
#     'latitudeChange': 0.13288419999999945,
#     'longitudeChange': 0.18917760000000783,
#     'kmNorthSouth': 4.203415642752733,
#     'kmEastWest': 21.035589354794546
# }

print(rent_canada_viewport_details)
print(rent_faster_viewport_details)
print(rent_seeker_viewport_details)
exit()
# step 2:
# use step 1 info to
# plan a grid in each city, for each provider
for provider in providers:
    provider_name = provider.name
    for city in cities:
        start_coords = city.get_center_coords()
        bounds = get_bounds_for(provider_name)
        grid = get_grid_plan(start_coords, bounds, provider.radius)
        # for entry in grid["gridCoords"]:
        #     print(provider_name)
        #     print(entry)
        # raise ValueError('pause')
        queue_payload = {
            "provider": provider_name,
            "cityName": city.name,
            "batchNum": 5,
            "zoomWidth": 13,
            # "coords": grid["gridCoords"],
            "coords": [start_coords],
        }
        if provider_name == "rentCanada":
            canada_grid_payloads.append(queue_payload)
        elif provider_name == "rentFaster":
            faster_grid_payloads.append(queue_payload)
        elif provider_name == "rentSeeker":
            seeker_grid_payloads.append(queue_payload)
        else:
            raise ValueError("Unexpected value")


# step 3:
# queue scans
for group in [seeker_grid_payloads, faster_grid_payloads, canada_grid_payloads]:
    for payload in group:
        print(payload, '184rm')
        pass_fail = queue_grid_scan(payload)
        print("Pass and fail:")
        print(pass_fail)

