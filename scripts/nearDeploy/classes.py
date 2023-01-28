
class City:
    def __init__(self, name, state, center_lat, center_long):
        self.name = name
        self.state = state
        self.long = center_long
        self.lat = center_lat

    def get_center_coords(self):
        return {"lat": self.lat, "long": self.long}

class Provider:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius  # radius controls the width of the scan. but "1" is still about 20x wider than needed.
        self.info = None

    def set_viewport_info(self, info):
        self.info = info

    def get_viewport_info(self):
        if self.info is not None:
            return self.info
        else:
            raise ValueError("info was none")


class Payload:
    def __init__(self, city):
        self.city_name = city
        self.provider = None
        self.bounds = None
        self.batch_num = None
        self.grid = None
        self.radius = 24  # just what it said in Postman

    def add_center(self, lat, long):
        self.long = long
        self.lat = lat
        return self

    def get_coords(self):
        return self.lat, self.long

    def set_provider(self, source):
        self.provider = source
        return self

    def store_bounds(self, bounds):
        self.bounds = bounds

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        if self.grid is not None:
            return self.grid
        else:
            raise ValueError("grid was none")

    def to_dict(self):
        return vars(self)
