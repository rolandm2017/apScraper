def calculate(value1, value2):
    if value1 > value2:
        return value1 - value2
    else:
        return value2 - value1

# "north":{"lat":45.553102184226546,"lng":-73.5512056051919},
# "south":{"lat":45.44661960947297,"lng":-73.63583466402979}}


long1 = -73.5512056051919
long2 = -73.63583466402979

lat1 = 45.553102184226546
lat2 = 45.44661960947297

print(calculate(lat1, lat2) / 2)
print(calculate(long1, long2) / 2)
