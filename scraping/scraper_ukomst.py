
import json
import requests
from bs4 import BeautifulSoup
import re

urls = ["https://app.catsone.nl/portal?id=4337"]

payload={}
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': '*/*'
}

response = requests.request("GET", urls[0], headers=headers, data=payload)
response_json = response.json()

with open('data/ukomst.json', 'w') as f:
    json.dump(response_json, f)

with open("data/ukomst.json", "r") as read_file:
    data = json.load(read_file)


job_list = []
for idx, job in enumerate(data['jobs']):
    job_info = {}
    if idx > 25:
        break
    job_info['Title'] = job['title']
    if '(' in job_info['Title']: #and re.match(r"(([a-z])+)([0-9]+)", job_info['Title'], re.I):
        temp_title = job_info['Title']
        job_info['Hours'] = temp_title.split('(')[1].replace(')','')
        job_info['Title'] = job_info['Title'].split('(')[0].strip()
    else:
        job_info['Hours'] = '40 uur'
    job_info['URL'] = job['url']
    job_info['Company'] = job['custom_fields'][1]['value']
    job_info['Location'] = job['location']['city']
    job_info['Description'] = job['description']

    job_info['Duration'] = job['duration']
    job_list.append(job_info)
print(job_list)
with open('data/ukomst_parsed.json', 'w') as f:
    json.dump(job_list, f)