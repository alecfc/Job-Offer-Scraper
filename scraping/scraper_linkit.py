import json
import requests
from bs4 import BeautifulSoup

url = "https://search.linkit.nl/linkit_vacancy/_msearch?"

payload = "{\"preference\":\"es-vacancy-list\"}\n{\"query\":{\"bool\":{\"must\":[{\"bool\":{\"must\":[{\"terms\":{\"type\":[\"Freelance\"]}}]}}]}},\"size\":25,\"_source\":{\"includes\":[\"*\"],\"excludes\":[]},\"from\":0,\"sort\":{\"created_at\":{\"order\":\"desc\",\"unmapped_type\":\"date\"}}}\n"
headers = {
  'Accept-Language': 'en,en-US;q=0.9,nl;q=0.8',
  'Connection': 'keep-alive',
  'Origin': 'https://www.linkit.nl',
  'Referer': 'https://www.linkit.nl/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'content-type': 'application/x-ndjson',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

html = response.text
response_json = response.json()

with open('data/linkit.json', 'w') as f:
    json.dump(response_json, f)

# Scrapping the Web (you can use 'html' or 'lxml')
soup = BeautifulSoup(html, 'lxml')

# Outer Most Entry Point of HTML:
outer_most_point=soup.find('div',{'class': 'Overview_overview__2bcF5'})
vacancy_list = outer_most_point.find('div', {'class': 'vacancies_vacancies__reactive-list__3q5G9'})
for i in outer_most_point.find('vacancies_vacancies__vacancy-list__3MhXB'):
    job_title=i.find('h2',{'class':'VacancyCard_vacancy-card__title__1DKYj'})
    print(job_title)

print(response.text)
