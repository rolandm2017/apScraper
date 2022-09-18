from .Provider import Provider

class MapBoundaries:
    def __init__(self, source):
        self.provider = source

    def make_boundaries(self, lat, long):
        if self.provider == Provider.rentCanada:
            lat_padding = 0.053241287376788904
            long_padding = 0.04231452941894531
        elif self.provider == Provider.rentFaster:
            lat_padding = 0.0978503023843551  # calculated in the distance.py file
            long_padding = 0.09698867797851562
        elif self.provider == Provider.rentSeeker:
            lat_padding = 0.0978503023843551  # calculated in the distance.py file
            long_padding = 0.09698867797851562
        else:
            raise ValueError("No provider given in MapBoundaries")

        lat_bound_up = lat + lat_padding  # calculated in the distance.py file
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding
        bounds_dict = {"north": lat_bound_up,
                       "south": lat_bound_down,
                       "east": long_bound_west,
                       "west": long_bound_east
                       }
        return bounds_dict

    def add_map_boundaries(self, lat1, long1, lat2, long2):
        if self.provider == Provider.rentCanada:
            pass
        elif self.provider == Provider.rentFaster:
            # I believe the 'l' value references (a) zoom level and (b) center of the map as lat,long
            return f"l=11%2C45.5017%2C-73.5673&" \
                   f"area=${lat1}%2C${long1}%2C${lat2}%2C${long2}&exclude="
        elif self.provider == Provider.rentSeeker:
            return '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&' \
                   'insideBoundingBox=%5B%5B${}%2C${}%2C${}%2C${}%5D"}'.format(lat1, long1, lat2, long2)
        else:
            raise ValueError("No provider given in MapBoundaries")