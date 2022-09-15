class MapBoundaries:
    def __init__(self, source):
        self.provider = source

    def assign(self, lat1, long1, lat2, long2):
        if self.provider == "rentCanada":
            pass
        elif self.provider == "rentFaster":
            # I believe the 'l' value references (a) zoom level and (b) center of the map as lat,long
            return f"l=11%2C45.5017%2C-73.5673&" \
                   f"area=${lat1}%2C${long1}%2C${lat2}%2C${long2}&exclude="
        elif self.provider == "rentSeeker":
            return '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&' \
                   'insideBoundingBox=%5B%5B${}%2C${}%2C${}%2C${}%5D"}'.format(lat1, long1, lat2, long2)
        else:
            pass