import requests
from flask import Flask, request, make_response
print("cats")
app = Flask(__name__)

# Last successful query made: Aug 1


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

    lat_padding = 0.053241287376788904
    long_padding = 0.04231452941894531

    lat_bound_up = lat + lat_padding  # calculated in the distance.py file
    lat_bound_down = lat - lat_padding
    long_bound_west = long + long_padding
    long_bound_east = long - long_padding

    start = make_query_string(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

    s = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    r = s.get(start, headers=headers)

    results = r.json()
    # print(text.json(), "19rm")

    # print(text.count("propertyId"))
    print(lat, long, len(results))
    return results


def make_query_string(lat1, long1, lat2, long2):
    # according to https://www.w3schools.com/tags/ref_urlencode.ASP
    # %22 = a double quote like "
    return (f"https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]"
            f"%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,"
            f"%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22"
            f"checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22"
            f"rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22"
            f"mapBounds%22:%7B%22"
            f"north%22:%7B%22lat%22:{lat1},%22lng%22:{long1}%7D,%22"
            f"south%22:%7B%22lat%22:{lat2},%22lng%22:{long2}%7D%7D,%22keyword%22:null,%22furnished%22:null%7D")
# original string: "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,
# %22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist
# %22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max
# %22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max
# %22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south
# %22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

# Example map box boundaries:
# "north":{"lat":45.553102184226546,"lng":-73.5512056051919},
# "south":{"lat":45.44661960947297,"lng":-73.63583466402979}}


# flask run -h localhost -p 5000
