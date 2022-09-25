import requests
from flask import Flask, request, make_response
print("horses")
app = Flask(__name__)

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # necessary so proxyTools folder is available
from util.ipgetter import get_proxy_ip
from util.checker import check_public_ip

# Last successful query made: Aug 1


@app.route("/")
def apartments():
    """
    Uses lat and long to query RentFaster.ca for apartments.
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

    start = "https://www.rentfaster.ca/api/map.json"

    s = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'PHPSESSID=2060b3eb3fe6ed290dcb19f3543741ec; _gcl_au=1.1.1167754990.1656991721; _ga=GA1.2.1983608871.1656991721; _gid=GA1.2.926434949.1656991721; _fbp=fb.1.1656991720812.932904256; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; lastcity=qc%2Fmontreal; _gat_UA-226906-1=1; _tac=false~google|not-available; _tas=jwhs0t4osgq'
    }

    cookie2 = 'PHPSESSID=7185b866aede45c4c76dde286033f60a; _gcl_au=1.1.1499582163.1659423039; _ga=GA1.2.727073008.1659423039; _gid=GA1.2.1767852712.1659423039; _gat_UA-226906-1=1; _fbp=fb.1.1659423038865.1488717403; _tac=false~self|not-available; _ta=ca~1~9de8a34ae94473607d23d07f7008d925; _tas=rrnc9ie7jv8; lastcity=qc%2Fmontreal'

    raw_text_body = add_map_boundaries(lat_bound_up, long_bound_west, lat_bound_down, long_bound_east)

    r = s.post(start, headers=headers, data=raw_text_body)  # its POST in this one

    results = r.json()
    print(lat, long, len(results))
    return results


def add_map_boundaries(lat1, long1, lat2, long2):
    # I believe the 'l' value references (a) zoom level and (b) center of the map as lat,long
    return f"l=11%2C45.5017%2C-73.5673&" \
           f"area=${lat1}%2C${long1}%2C${lat2}%2C${long2}&exclude="

# flask run -h localhost -p 5002
