import requests

urls = ["https://app.catsone.nl/portal?id=4337"]

payload={}
headers = {
  'accept': '*/*'
}

response = requests.request("GET", urls[0], headers=headers, data=payload)

print(response.text)
