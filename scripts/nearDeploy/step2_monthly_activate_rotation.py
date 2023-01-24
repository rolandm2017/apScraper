import requests
import os
import datetime

# Should be scheduled to run on the 1st, 8th, and 15th

PROD_OR_DEV = os.environ.get("PROD_OR_DEV")

is_prod = PROD_OR_DEV is "prod" or PROD_OR_DEV is "production"
is_dev = PROD_OR_DEV is "dev" or PROD_OR_DEV is "development"

if PROD_OR_DEV is None:
    raise RuntimeError("Failed to load environment variable")

if is_dev is not True and is_prod is not True:
    raise RuntimeError("Failed to set proper env variable")

# Rotation:
# We scrape every city once every week, with one off week at the end of the month.
# The scraping per city is done via rotation:
# RentCanada takes Vancouver, Toronto, Montreal
# RentFaster takes Calgary, Mississauga, Ottawa
# RentSeeker takes Edmonton, Winnipeg, Brampton, Hamilton
# Next week, the jobs are rotated.
# This way, we don't hit any particular provider too hard.

# Payload("Vancouver", "British Columbia").add_center(49.2827, -123.1207),  # 1
# Payload("Calgary", "Alberta").add_center(51.0447, -114.0719),  # 2
# Payload("Edmonton", "Alberta").add_center(53.5461, -113.4937),  # 3
# Payload("Winnipeg", "Manitoba").add_center(49.8954, -97.1385),  # 4
# Payload("Toronto", "Ontario").add_center(43.6532, -79.3832),  # 5
# Payload("Mississauga", "Ontario").add_center(43.589, -79.6441),  # 6
# Payload("Brampton", "Ontario").add_center(43.7315, -79.7624),  # 7
# Payload("Hamilton", "Ontario").add_center(43.2557, -79.8711),  # 8
# Payload("Ottawa", "Ontario").add_center(45.4215, -75.6972),  # 9
# Payload("Montreal", "Quebec").add_center(49.2827, -123.1207),  # 10


class Rotation:
    def __init__(self, provider, cities):
        self.provider = provider
        self.cities = cities

    def get_cities(self):
        return self.cities


day_one = [
    Rotation("rentCanada", ["Vancouver", "Toronto", "Montreal"]),
    Rotation("rentFaster", ["Calgary", "Mississauga", "Ottawa"]),
    Rotation("rentSeeker", ["Edmonton", "Winnipeg", "Brampton", "Hamilton"]),
]


day_eleven = [
    Rotation("rentFaster", ["Vancouver", "Toronto", "Montreal"]),
    Rotation("rentSeeker", ["Calgary", "Mississauga", "Ottawa"]),
    Rotation("rentCanada", ["Edmonton", "Winnipeg", "Brampton", "Hamilton"]),
]


day_twenty_one = [
    Rotation("rentSeeker", ["Vancouver", "Toronto", "Montreal"]),
    Rotation("rentCanada", ["Calgary", "Mississauga", "Ottawa"]),
    Rotation("rentFaster", ["Edmonton", "Winnipeg", "Brampton", "Hamilton"]),
]

activate_url = "http://127.0.0.1:5000/activate"
prod_activate_url = ""

current_day = datetime.now().day

# integers are days of the month.
rotation_day_one = 0 < current_day < 4
rotation_day_eleven = 7 < current_day < 12
rotation_day_twenty_one = 14 < current_day < 18


def make_activate_request(url, city_request):
    request = requests.post(url, data=city_request)
    activated = request.json()
    print(activated, "for city:", city_request)


if rotation_day_one:
    for rotation in day_one:
        for city in rotation.get_cities():
            make_activate_request(activate_url, city)

if rotation_day_eleven:
    for rotation in day_eleven:
        for city in rotation.get_cities():
            make_activate_request(activate_url, city)

if rotation_day_twenty_one:
    for rotation in day_twenty_one:
        for city in rotation.get_cities():
            make_activate_request(activate_url, city)

print("Done rotation")
