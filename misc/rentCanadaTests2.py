x = f"https://www.rentcanada.com/api/listings?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22" \
    f"checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22" \
    f"rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22" \
    f"checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22" \
    f"min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22" \
    f"mapBounds%22:%7B%22" \
    f"north%22:%7B%22lat%22:45.464187504106135,%22lng%22:-73.60059282238653%7D,%22" \
    f"south%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D%7D,%22" \
    f"keyword%22:null,%22furnished%22:null%7D"

y = f"https://www.rentcanada.com/api/listings?filters=%7B%22amenities%22:%7B%22" \
    f"checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22" \
    f"rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22" \
    f"checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22" \
    f"min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22" \
    f"mapBounds%22:%7B%22" \
    f"north%22:%7B%22lat%22:45.464187504106135,%22lng%22:-73.60059282238653%7D,%22" \
    f"south%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D%7D,%22" \
    f"keyword%22:null,%22furnished%22:null%7D"

a = f""


import requests

# All of montreal

# Request URL: https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D,%22south%22:%7B%22lat%22:45.49077609093645,%22lng%22:-73.57162496502569%7D%7D,%22keyword%22:null,%22furnished%22:null%7D
addr = "https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

page_num = 4
working_query = f"https://www.rentcanada.com/api/listings?page={page_num}&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

working_query2 = f"https://www.rentcanada.com/api/listings?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

# 22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D
# lat1 = 45.553102184226546
# long1 = -73.5512056051919
# lat2 = 45.44661960947297
# long2 = -73.63583466402979

lat1 = 45.49077609093645   # smaller
lat2 = 45.54395326459708

long1 = -73.57162496502569  # smaller
long2 = -73.51368925030401



working_query3 = f"https://www.rentcanada.com/api/listings?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:{lat1},%22lng%22:{long1}%7D,%22south%22:%7B%22lat%22:{lat2},%22lng%22:{long2}%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
#
# def make_query_string(page_num):
#     url =
#     return url


s = requests.Session()
headers = {
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
r = s.get(working_query3, headers=headers)

print(r.json())