# This file calculates the distance from the center of a map view to the borders of it
# by taking the lat,long of all the apartments and sorting out, "which is the westernmost point?"
# "which is the eastmost point? Which is the furthest north, south?"
# and then dividing by 2 to get the distance from the middle to the right and left, top and bottom

def calculate(value1, value2):
    if value1 > value2:
        return value1 - value2
    else:
        return value2 - value1

# RentCanada values for box perimeter
# "north":{"lat":45.553102184226546,"lng":-73.5512056051919},
# "south":{"lat":45.44661960947297,"lng":-73.63583466402979}}

long1 = -73.5512056051919  # where did these values come from?
long2 = -73.63583466402979

lat1 = 45.553102184226546
lat2 = 45.44661960947297

print("== RentCanada ==")
# print(calculate(lat1, lat2) / 2)
# print(calculate(long1, long2) / 2)

# RentSeeker values for box perimeter
# [[45.45344020494669,-73.65633240761402,45.6491408097154,-73.46235505165698]]

lat1 = 45.45344020494669
lat2 = 45.6491408097154

long1 = -73.65633240761402
long2 = -73.46235505165698

print("== RentSeeker ==")
# print(calculate(lat1, lat2) / 2)
# print(calculate(long1, long2) / 2)

# RentFaster values for box perimeter

# Values 1
# l: 11,45.5017,-73.5673
# area: 45.697472580722355,-73.3300639770508,45.30524429537341,-73.80453602294924

# Values 2
# l: 13,45.5099,-73.5363
# area: 45.55894101069567,-73.48524586181642,45.460898299752024,-73.58738438110353

lat1 = 45.697472580722355
lat2 = 45.30524429537341

long1 = -73.3300639770508
long2 = -73.80453602294924

lat3 = 45.55894101069567
lat4 = 45.460898299752024
long3 = -73.48524586181642
long4 = -73.58738438110353

print("== RentFaster ==")
# print(calculate(lat1, lat2))
# print(calculate(long1, long2))
# print(calculate(lat3, lat4))
# print(calculate(long3, long4))

# == RentCanada ==
# 0.053241287376788904
# 0.04231452941894531
# == RentSeeker ==
# 0.0978503023843551
# 0.09698867797851562
# == RentFaster ==
# 0.39222828534894205
# 0.4744720458984375
# 0.0980427109436448  # lat is 1/4 wide as prev value -- I zoomed in twice
# 0.10213851928710938  # long is 10/47 as wide as prev value (2x zoom)


