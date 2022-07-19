to scrape apartments.com, you need to

1. send a post request to https://www.apartments.com/services/search/

2. make the body be like

{
    "Map": {
        "BoundingBox": {
            "UpperLeft": {
                "Latitude": 48.00979493852227,
                "Longitude": -122.6680605593109
            },
            "LowerRight": {
                "Latitude": 47.25185572090765,
                "Longitude": -122.05557276634215
            }
        },
        "CountryCode": "US",
        "Shape": null
    },
    "Geography": {
        "ID": "wyllkch",
        "Display": "Seattle, WA",
        "GeographyType": 2,
        "Address": {
            "City": "Seattle",
            "State": "WA",
            "MarketName": "Seattle",
            "DMA": "Seattle-Tacoma, WA"
        },
        "Location": {
            "Latitude": 47.615,
            "Longitude": -122.336
        },
        "BoundingBox": {
            "LowerRight": {
                "Latitude": 47.49555,
                "Longitude": -122.23591
            },
            "UpperLeft": {
                "Latitude": 47.73414,
                "Longitude": -122.43623
            }
        },
        "v": 17050
    },
    "Listing": {},
    "Paging": {
        "Page": null
    },
    "IsBoundedSearch": true,
    "ResultSeed": 101995,
    "Options": 0
}

3. get a x_csrf_token from a REAL request made to "search/" in the network tab of, say, https://www.apartments.com/seattle-wa/?bb=96y_lmr1vQg85pjsJ

4. the data comes in as 

"PinsState": {
        "cl"

5. You have to decode the data. 