import requests
from flask import Flask, request, make_response
print("cats")
app = Flask(__name__)

@app.route("/")
def apartments():
    """
    Uses lat and long to query RentCanada.com for apartments.
    Translation from city,state,country to lat and long must be done prior to this step.
    NOTE: In RentCanada's coordinate system, West is negative, East is positive.
    :return: A list of gyms.
    """
    location = request.json
    # city = location["city"]
    # state = location["state"]
    # country = location["country"]
    lat = location["lat"]
    long = location["long"]

    start = make_query_string(lat, long)

    s = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    r = s.get(start, headers=headers)

    apartments = r.json()
    # print(text.json(), "19rm")

    # print(text.count("propertyId"))
    print(len(text))
    return apartments


def make_query_string(lat, long):
    return f"https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:{lat},%22lng%22:{long}%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
# original string: "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
