from .Provider import Provider

class QueryString:
    def __init__(self, source):
        self.provider = source

    def make_query_string(self, lat1, long1, lat2, long2):
        if self.provider == None:
            raise ValueError("No provider added to QueryString class")

        if self.provider == Provider.rentCanada:
            return (f"https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]"
                    f"%7D,%22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,"
                    f"%22rentalTypes%22:%7B%22checklist%22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22"
                    f"checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22"
                    f"rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max%22:null%7D,%22"
                    f"mapBounds%22:%7B%22"
                    f"north%22:%7B%22lat%22:{lat1},%22lng%22:{long1}%7D,%22"
                    f"south%22:%7B%22lat%22:{lat2},%22lng%22:{long2}%7D%7D,%22keyword%22:null,%22furnished%22:null%7D")
        # original string: "https://www.rentcanada.com/api/map-markers?filters=%7B%22amenities%22:%7B%22checklist%22:[]%7D,
        # %22utilities%22:%7B%22checklist%22:[]%7D,%22petPolicies%22:%7B%22checklist%22:[]%7D,%22rentalTypes%22:%7B%22checklist
        # %22:[]%7D,%22beds%22:%7B%22min%22:null,%22max%22:null,%22checklist%22:[]%7D,%22baths%22:%7B%22min%22:null,%22max
        # %22:null,%22checklist%22:[]%7D,%22rates%22:%7B%22min%22:null,%22max%22:null%7D,%22sqft%22:%7B%22min%22:null,%22max
        # %22:null%7D,%22mapBounds%22:%7B%22north%22:%7B%22lat%22:45.553102184226546,%22lng%22:-73.5512056051919%7D,%22south
        # %22:%7B%22lat%22:45.44661960947297,%22lng%22:-73.63583466402979%7D%7D,%22keyword%22:null,%22furnished%22:null%7D"

        if self.provider == Provider.rentFaster:
            raise ValueError("No implementation for rentFaster")

        if self.provider == Provider.rentSeeker:
            return f"https://8hvk5i2wd9-dsn.algolia.net/1/indexes/rentseeker_prod_properties/" \
                   f"query?" \
                   f"x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&" \
                   f"x-algolia-application-id=8HVK5I2WD9&" \
                   f"x-algolia-api-key=68a749c1cd4aff1ca2c87a160617bd61"

