import requests


def make_loc_dict(city_name, state):
    return {
        "cityName": city_name,
        "state": state,
        "country": "Canada"
    }


location_dicts = [
    make_loc_dict("Vancouver", "British Columbia"),
    make_loc_dict("Calgary", "Alberta"),
    make_loc_dict("Edmonton", "Alberta"),
    make_loc_dict("Winnipeg", "Manitoba"),
    make_loc_dict("Toronto", "Ontario"),
    make_loc_dict("Ottawa", "Ontario"),
    make_loc_dict("Mississauga", "Ontario"),
    make_loc_dict("Brampton", "Ontario"),
    make_loc_dict("Hamilton", "Ontario"),
    make_loc_dict("Montreal", "Quebec")
]

for loc in location_dicts:
    url = f"http://127.0.0.1:8000/google/gyms?cityName={loc['cityName']}&state={loc['state']}&country={loc['country']}"
    r = requests.get(url)
    print(r.json())


