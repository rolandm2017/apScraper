import requests

activate_url = "http://127.0.0.1:5000/activate"
# the endpoint we hit to tell the scraper to
# 1. get tasks
# 2. scrape the tasks
# 3. send the scraped data to the server

data_rent_canada = {
    "provider": "rentCanada"
}

data_rent_faster = {
    "provider": "rentFaster"
}

data_rent_seeker = {
    "provider": "rentSeeker"
}

activate_request1 = requests.post(activate_url, json=data_rent_canada)
activate_request2 = requests.post(activate_url, json=data_rent_faster)
activate_request3 = requests.post(activate_url, json=data_rent_seeker)


