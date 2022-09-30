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

t = f'{"amenities":{"checklist":[]},"utilities":{"checklist":[]},"petPolicies":{"checklist":[]},"rentalTypes":{"checklist":[]},"beds":{"min":null,"max":null,"checklist":[]},"baths":{"min":null,"max":null,"checklist":[]},"rates":{"min":null,"max":null},"sqft":{"min":null,"max":null},"mapBounds":{"north":{"lat":45.53888757573557,"lng":-73.54428136062885},"south":{"lat":45.439168665456790,"lng":-73.62238728718882}},"keyword":null,"furnished":null}'
#
#
# print(len(x), len(y))
#
# zipper = ""
# for char in range(0, len(x)):
#     if x[char] == y[char]:
#         # print(x[char], y[char])
#         pass
#     else:
#         print(x[char], y[char])

import requests

# All of montreal

# Request URL: https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D,%22south%22:%7B%22lat%22:45.49077609093645,%22lng%22:-73.57162496502569%7D%7D,%22keyword%22:null,%22furnished%22:null%7D
addr = "https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"


def make_query_string(page_num):
    url = f"https://www.rentcanada.com/api/listings?page={page_num}&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south%22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
    return url


s = requests.Session()
headers = {
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
r = s.get(addr, headers=headers)

# print(r.text)

scraped_apartments = []

for i in range(0, 15):
    query = make_query_string(i)
    r = s.get(query, headers=headers)
    print(query, r)
    file_name = f"stealings_{i}.txt"
    with open(file_name, "w") as f:
        f.write(r.text)
