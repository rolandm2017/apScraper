from ..scrapers.Provider import Provider
from ..api.websitesAPI import WebsitesAPI
from ..util.proxyTools import ProxyTools
from ..scrapers.MapBoundaries import MapBoundaries
from ..scrapers.QueryString import QueryString

# north%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D,%22south%22:%7B%22lat%22:45.49077609093645,%22lng%22:-73.57162496502569%7D
north_lat = 45.517364677766764
north_long = -73.54265710766485
south_lat = 45.49077609093645
south_long = -73.57162496502569
start = "https://www.rentcanada.com/api/listings?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D,%22south%22:%7B%22lat%22:45.49077609093645,%22lng%22:-73.57162496502569%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

north2_lat = north_lat - 0.005
north2_long = north_long - 0.005
south2_lat = south_lat - 0.005
south2_long = south_long - 0.005

def use_websites_API_like_in_scraper(lat, long):
    provider = Provider("rentCanada")
    bounds = MapBoundaries(provider.type).make_boundaries(lat, long)
    start = QueryString(provider.type).make_query_string(bounds["north"], bounds["west"], bounds["south"],
                                                         bounds["east"])

    ip, port = ProxyTools().get_proxy_ip(0)
    proxy_dict = ProxyTools().create_proxy_dict(ip, port)

    return WebsitesAPI(provider.type).scrape_rent_canada(start, proxy_dict)

def use_websites_API(input_string):
    provider = Provider("rentCanada")
    ip, port = ProxyTools().get_proxy_ip(0)
    proxy_dict = ProxyTools().create_proxy_dict(ip, port)
    return WebsitesAPI(provider.type).scrape_rent_canada(input_string, proxy_dict)

def test_websites_API():
    results = use_websites_API(start)
    # print(results)
    assert len(results["listings"]) == 34

def test_use_websites_api_like_in_scraper():
    results = use_websites_API_like_in_scraper(north_lat, north_long)
    print(results)
    assert len(results["listings"]) > 0

def test_2():
    results = use_websites_API_like_in_scraper(south_lat, south_long)
    print(results)
    assert len(results["listings"]) > 0

def test_3():
    results = use_websites_API_like_in_scraper(north2_lat, north2_long)
    print(results)
    assert len(results["listings"]) > 0

def test_4():
    results = use_websites_API_like_in_scraper(south2_lat, south2_long)
    print(results)
    assert len(results["listings"]) > 0
