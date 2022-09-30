north_lat = 45.517364677766764
north_long = -73.54265710766485
south_lat = 45.49077609093645
south_long = -73.57162496502569

def bump_lat(original_lat_1, original_lat_2, start_lat):
    # works for longitude too
    distance = abs(original_lat_1 - original_lat_2)
    left = start_lat - distance
    right = start_lat + distance
    return left, right

def custom_query_string(lat, long):
    new_lats = bump_lat(north_lat, south_lat, lat)
    new_longs = bump_lat(north_long, south_long, long)

    print(new_longs, new_lats)
    # original string values
    # f"%22north%22:%7B%22lat%22:45.517364677766764,%22lng%22:-73.54265710766485%7D," \
    # f"%22south%22:%7B%22lat%22:45.49077609093645,%22lng%22:-73.57162496502569%7D%7D," \
    s = f"https://www.rentcanada.com/api/listings" \
        f"?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D," \
        f"%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D," \
        f"%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null," \
        f"%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D," \
        f"%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%" \
        f"22mapBounds%22:%7B" \
        f"%22north%22:%7B%22lat%22:{new_lats[0]},%22lng%22:{new_longs[0]}%7D," \
        f"%22south%22:%7B%22lat%22:{new_lats[1]},%22lng%22:{new_longs[1]}%7D%7D," \
        f"%22keyword%22:null,%22furnished%22:null%7D"
    return s

# why did i make this file
# its so i can use it for a more crude api test

# print(custom_query_string(north_lat, north_long))
# print(custom_query_string(south_lat, south_long))
print(bump_lat(north_lat, south_lat, north_lat))
print(bump_lat(north_long, south_long, north_long))