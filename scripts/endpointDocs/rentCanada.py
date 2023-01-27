import json
from translator import translate_to_english

v1 = "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.5958025755942,%22lng%22:-73.5348325841574%7D,%22south%22:%7B%22lat%22:45.39726422634626,%22lng%22:-73.68383465935271%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
v1listings = "https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.5958025755942,%22lng%22:-73.5348325841574%7D,%22south%22:%7B%22lat%22:45.39726422634626,%22lng%22:-73.68383465935271%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
# i move the map now and it reloads more stuff
v2 = "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.54623361211241,%22lng%22:-73.57026065369764%7D,%22south%22:%7B%22lat%22:45.44696443880251,%22lng%22:-73.6447616912953%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
v2listings = "https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.54623361211241,%22lng%22:-73.57026065369764%7D,%22south%22:%7B%22lat%22:45.44696443880251,%22lng%22:-73.6447616912953%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

# i zoom in a third time
v3 = "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.52143272483987,%22lng%22:-73.58888591309706%7D,%22south%22:%7B%22lat%22:45.47179813834915,%22lng%22:-73.62613643189589%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"
v3listings = "https://www.rentcanada.com/api/listings?page=1&listingsLedger=%7B%7D&filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.52143272483987,%22lng%22:-73.58888591309706%7D,%22south%22:%7B%22lat%22:45.47179813834915,%22lng%22:-73.62613643189589%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

t1 = translate_to_english(v1)
t1l = translate_to_english(v1listings)

print("#######\n#######\n#########\n\n")

t2 = translate_to_english(v2)
t2l = translate_to_english(v2listings)

print("#######\n#######\n#########\n\n")

t3 = translate_to_english(v3)
t3l = translate_to_english(v3listings)

# I expect the long lat and zoomwidth will be revealed in prints.


def get_bounds(query):
    middle = query.split('mapBounds":{')[1]
    isolated_from_end = middle.split(',"keyword')[0]
    # here is the boundign box
    return isolated_from_end


t1b = get_bounds(t1)
t1lb = get_bounds(t1l)
t2b = get_bounds(t2)
t3b = get_bounds(t3)
print(t1b)
print(t2b)
print(t3b)


def get_north(bounds):
    isolated = bounds.split('"north":')[1].split(',"south')[0]
    print(isolated)
    dumped = json.loads(isolated)
    return dumped

def get_south(bounds):
    isolated = bounds.split('south":')[1][:-1]
    print(isolated)
    dumped = json.loads(isolated)
    return dumped

north1 = get_north(t1b)
north2 = get_north(t2b)
north3 = get_north(t3b)
south1 = get_south(t1b)
south2 = get_south(t2b)
south3 = get_south(t3b)
### win?
print(north1, south1)
print(north2, south2)
print(north3, south3)

lat1 = north1['lat']
lat2 = south1['lat']
long1 = north1['lng']
long2 = south1['lng']
print(lat1 - lat2, long1 - long2)  # 0.19853834924794 0.1490020751953125
# north1.lat > south1.lat, north1.long > south1.long

# conclusion: if i change the values for north and south to be a
# large square, I'll aim the viewport. north is northeast corner, south is southwest corner.
