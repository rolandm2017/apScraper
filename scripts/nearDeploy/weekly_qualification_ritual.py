import requests
import os
import datetime

# don't need to specify the time on this one


cities = [
    "Vancouver",
    "Calgary",
    "Edmonton",
    "Winnipeg",
    "Toronto",
    "Brampton",
    "Mississauga",
    "Hamilton",
    "Ottawa",
    "Montreal"
]

qualification_url = "http://127.0.0.1:8000/housing/qualify"
delete_unqualified_url = "http://127.0.0.1:8000/housing/unqualified"

def request_qualification(url, requested_city):
    response = requests.get(url, params={"cityName": requested_city})
    response_details = response.json()
    return response_details


def request_delete_unqualified(url, requested_city):
    response = requests.delete(url, params={"cityName": requested_city})
    response_details = response.json()
    return response_details


for city in cities:
    qualification_details = request_qualification(qualification_url, city)

for city in cities:
    deleted_apartments_details = request_delete_unqualified(delete_unqualified_url, city)

