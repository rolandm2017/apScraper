tar_url = 'https://www.rentfaster.ca/api/map.json'

p1 = "l=11%2C45.3902%2C-73.5088&area=45.57384111972111%2C-73.19057049164543%2C45.20591177222008%2C-73.82709087738762&e=zoom_changed&exclude="
p2 = "l=12%2C45.4219%2C-73.5651&area=45.51372840372307%2C-73.40583385834465%2C45.32986693146944%2C-73.72409405121574&e=zoom_changed&exclude="
p3 = "l=13%2C45.4581%2C-73.5716&area=45.50404250896503%2C-73.49199619272699%2C45.41217082255017%2C-73.65112628916253&e=zoom_changed&exclude="
# look at the "l" value

from translator import translate_to_english

p1t = translate_to_english(p1)  # l=11,45.3902,-73.5088&area=45.57384111972111,-73.19057049164543,45.205911772220084,-73.82709087738762&e=zoom_changed&exclude=
print(p1t)
print("######\n######\n")
p2t = translate_to_english(p2)
print(p2t)
print("######\n######\n")
p3t = translate_to_english(p3)
print(p3t)

def get_coords(jibberish):
    middle = jibberish.split('area=')[1]
    isolated = middle.split("&e=")[0]
    return isolated

study1 = get_coords(p1t)
study2 = get_coords(p2t)
study3 = get_coords(p3t)
print(study1)
print(study2)
print(study3)
# i expect this payload is all i need to aim the map

def get_lats(study):
    split = study.split(",")
    return float(split[0]), float(split[2])

def get_longs(study):
    split = study.split(",")
    return float(split[1]), float(split[3])

s1lats = get_lats(study1)
s1longs = get_longs(study1)
s2lats = get_lats(study2)
s2longs = get_longs(study2)
s3lats = get_lats(study3)
s3longs = get_longs(study3)

def area_of_square(lats, longs):
    width = abs(abs(longs[0]) - abs(longs[1]))
    height = abs(abs(lats[0]) - abs(lats[1]))
    print(f"area: {width * height}")


def check_l_val_is_middle(start_url, lats, longs):
    # l=11,45.3902,-73.5088&area
    without_area = start_url.split("&area")[0]
    without_l_val = without_area[4:]
    print(without_l_val)
    lat_long = without_l_val.split(",")[1:]
    lat = float(lat_long[0])
    long = float(lat_long[1])
    print("are they close to equal")
    a = lats[0] - lat
    a1 = lats[1] - lat
    b = longs[0] - long
    b1 = longs[1] - long
    print(a, a1)
    print(b, b1)
    print(a + a1)
    print(b + b1)   # yes they are close to equal
    print("########\n#######\n#######\n")


lat_diff1 = s1lats[0] - s1lats[1]
long_diff1 = s1longs[0] - s1longs[1]


lat_diff2 = s2lats[0] - s2lats[1]
long_diff2 = s2longs[0] - s2longs[1]

lat_diff3 = s3lats[0] - s3lats[1]
long_diff3 = s3longs[0] - s3longs[1]
print("diff p1")
print(lat_diff1, long_diff1)
check_l_val_is_middle(p1t, s1lats, s1longs)

print("diff p2")
print(lat_diff2, long_diff2)
check_l_val_is_middle(p2t, s2lats, s2longs)
print("diff p3")
print(lat_diff3, long_diff3)
check_l_val_is_middle(p3t, s3lats, s3longs)



# conclusion: draw a square. send a 4 decimal # to the L value. Position the viewport as a square, again.
area_of_square(s1lats, s1longs)
area_of_square(s2lats, s2longs)
area_of_square(s3lats, s3longs)
# area: 0.23419453019722408
# area: 0.058515787621004185
# area: 0.014619550318892196
