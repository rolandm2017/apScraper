# The Apartments Near Gyms Web Scraper

This is the web scraper for the Apartments Near Gyms website.

The web scraper is usable as an independent program to scrape apartment data from popular Canadian apartment rental websites. Or it can be used in tandem with the rest of the backend to plan a Canada-wide scrape of the websites. 

The scraper makes use of Celery to run several concurrent threads, decreasing scraping time from days to a few hours. This could happen even faster but I wanted to be nice to their servers! :-)

You can view the frontend for the Apartments Near Gyms program here: https://github.com/plutownium/gymsFE

And the rest of the backend for it here: https://github.com/plutownium/gymSaas

Happy reading!