from ..scrapers.Scraper import Scraper


# ### Arrange
# Pretend oneShot route
def one_shot():
    scrape_details = {"lat": 45, "long": -73, "provider": "rentCanada"}
    scraper = Scraper("rentCanada")
    scraper.refresh_proxy()
    results = scraper.scrape(scrape_details)  # Todo: modify scraper to take mocks for api
    return results


# ### Act
# def test_one_shot():
#     assert one_shot() == 5

