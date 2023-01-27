from .Provider import Provider

from canadaAps.util.convertURLEntities import translate_to_english

class MapBoundaries:
    def __init__(self, source):
        self.provider = source

    def make_boundaries(self, lat, long):
        if self.provider.type == Provider.rentCanada:
            # 01/26 zombied
            # lat_padding = 0.053241287376788904
            # long_padding = 0.04231452941894531
            lat_padding = 0.053241287376788904 - 0.02  # - 0.02 made the viewport narrower! Yay
            long_padding = 0.04231452941894531 - 0.02
        elif self.provider.type == Provider.rentFaster:
            lat_padding = 0.0978503023843551  # calculated in the distance.py file
            long_padding = 0.09698867797851562
        elif self.provider.type == Provider.rentSeeker:
            lat_padding = 0.0978503023843551  # calculated in the distance.py file
            long_padding = 0.09698867797851562
        else:
            raise ValueError("No provider given in MapBoundaries")

        lat_bound_up = lat + lat_padding
        lat_bound_down = lat - lat_padding
        long_bound_west = long + long_padding
        long_bound_east = long - long_padding
        # if self.provider == Provider.rentCanada:

        bounds_dict = {"north": lat_bound_up,
                   "south": lat_bound_down,
                   "east": long_bound_east,
                   "west": long_bound_west
                   }
            # return
        return bounds_dict

    def add_map_boundaries(self, lat1, long1, lat2, long2, viewport_width):

        if self.provider.get_type() == Provider.rentCanada:
            pass
        elif self.provider.get_type() == Provider.rentFaster:
            print(f"trying {self.provider.get_type()} with viewport width {viewport_width}")
            # I believe the 'l' value references (a) zoom level and (b) center of the map as lat,long
            # 01/26 - original string started 'l=11%2c45' before changing it to add viewport_width.
            center_lat = (lat1 + lat2) / 2
            center_long = (long1 + long2) / 2
            center_lat_four_decimals = float(str(center_lat)[0:7])
            center_long_four_decimals = float(str(center_long)[0:8])
            print(center_lat, center_long, '46rm')
            # return "l=13%2C45.4581%2C-73.5716&area=45.50404250896503%2C-73.49199619272699%2C45.41217082255017%2C-73.65112628916253&e=zoom_changed&exclude="
            url_with_strange_chars = f"l={viewport_width}%2C{center_lat_four_decimals}%2C{center_long_four_decimals}&" \
                   f"area=${lat1}%2C${long1}%2C${lat2}%2C${long2}&exclude="
            print("add_map_boundaries output")
            print(translate_to_english(url_with_strange_chars))
            return url_with_strange_chars
        elif self.provider.get_type() == Provider.rentSeeker:
            print(f"trying {self.provider.get_type()} with viewport width {viewport_width}")

            # note: Is there a problem here? See Postman "Ap Scraping Via Postman" / "RentSeeker.ca" / ...
            # Note2 01/26: lat2,long2, lat1, long1 reflects the swLatLong, neLatLong format of the actual website
            params_with_strange_chars = "query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=[[" + str(lat2) + "," + str(long2) + "," + str(lat1) + "," + str(long1) + "]]"
            print("add_map_boundaries output")
            print(translate_to_english(params_with_strange_chars))
            return {"params": params_with_strange_chars}
        else:
            raise ValueError("No provider given in MapBoundaries")
