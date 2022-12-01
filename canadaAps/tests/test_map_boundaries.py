from ..scraper.MapBoundaries import MapBoundaries
from ..scraper.QueryString import QueryString
from ..scraper.Provider import Provider

rent_canada_provider = Provider("rentCanada")
rent_faster_provider = Provider("rentFaster")
rent_seeker_provider = Provider("rentSeeker")


def arrange_rent_canada():
    bounds = MapBoundaries(rent_canada_provider).make_boundaries(10, -10)
    start = QueryString(rent_canada_provider).make_query_string(bounds["north"], bounds["west"], bounds["south"], bounds["east"])
    return bounds, start  # process over


def arrange_rent_faster():
    bounds = MapBoundaries(rent_faster_provider).make_boundaries(10, -10)
    raw_text_body = MapBoundaries(rent_faster_provider).add_map_boundaries(bounds["north"],
                                                                           bounds["west"],
                                                                           bounds["south"],
                                                                           bounds["east"])
    return bounds, raw_text_body  # process over


def arrange_rent_seeker():
    bounds = MapBoundaries(rent_seeker_provider).make_boundaries(10, -10)
    start = QueryString(rent_seeker_provider).make_query_string(bounds["north"],
                                                                bounds["west"],
                                                                bounds["south"],
                                                                bounds["east"])
    raw_json_body = MapBoundaries(rent_seeker_provider).add_map_boundaries(bounds["north"],
                                                                           bounds["west"],
                                                                           bounds["south"],
                                                                           bounds["east"])
    return bounds, start, raw_json_body  # process over


def test_rent_canada():
    bounds, start = arrange_rent_canada()
    assert "north" in bounds
    assert "east" in bounds
    assert "west" in bounds
    assert "south" in bounds
    assert len(start) == 666  # fixme: what is this REALLY testing?


def test_rent_faster():
    bounds, raw_text_body = arrange_rent_faster()
    assert "north" in bounds
    assert "east" in bounds
    assert "west" in bounds
    assert "south" in bounds
    assert len(raw_text_body) == 125  # fixme: what is this REALLY testing?


def test_rent_seeker():
    bounds, start, raw_json_body = arrange_rent_seeker()
    assert "north" in bounds
    assert "east" in bounds
    assert "west" in bounds
    assert "south" in bounds
    assert len(start) == 231
    assert len(raw_json_body["params"]) == 177  # fixme: what is this REALLY testing?

