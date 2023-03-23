
import json
import requests
from bs4 import BeautifulSoup

urls = ["https://app.catsone.nl/portal?id=4337"]

payload={}
headers = {
  'accept': '*/*'
}

response = requests.request("GET", urls[0], headers=headers, data=payload)
response_json = response.json()

with open('data/ukomst.json', 'w') as f:
    json.dump(response_json, f)
