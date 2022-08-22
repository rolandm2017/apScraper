import requests
from flask import Flask, request, make_response
print("dogs")
app = Flask(__name__)

# Last successful query made: Aug 1


@app.route("/")
def apartments():
    """
    Uses lat and long to query RentCanada.com for apartments.
    Translation from city,state,country to lat and long must be done prior to this step.

    :return: A list of gyms.
    """

    location = request.json
    # city = location["city"]
    # state = location["state"]
    # country = location["country"]
    lat = location["lat"]
    long = location["long"]

    lat_padding = 0.0978503023843551  # calculated in the distance.py file
    long_padding = 0.09698867797851562

    lat_bound_up = lat + lat_padding
    lat_bound_down = lat - lat_padding
    long_bound_west = long + long_padding
    long_bound_east = long - long_padding

    start = make_query_string()

    s = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    # raw_JSON_body = '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=%5B%5B45.45344020494669%2C-73.65633240761402%2C45.6491408097154%2C-73.46235505165698%5D%5D"}'
    raw_json_body = add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

    r = s.post(start, headers=headers, data=raw_json_body)  # its POST in this one

    results = r.json()
    print(lat, long, len(results))
    return results


def make_query_string():
    return f"https://8hvk5i2wd9-dsn.algolia.net/1/indexes/rentseeker_prod_properties/" \
           f"query?" \
           f"x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&" \
           f"x-algolia-application-id=8HVK5I2WD9&" \
           f"x-algolia-api-key=68a749c1cd4aff1ca2c87a160617bd61"


def add_map_boundaries(lat1, long1, lat2, long2):
    return '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&' \
            'insideBoundingBox=%5B%5B${}%2C${}%2C${}%2C${}%5D"}'.format(lat1, long1, lat2, long2)


# flask run -h localhost -p 5001
