import requests

s = requests.Session();

headers = {
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}


r = s.get("https://www.apartments.com/montreal-qc/", headers=headers)
print(r.text)

# TODO: make a successful query like in scraper.py