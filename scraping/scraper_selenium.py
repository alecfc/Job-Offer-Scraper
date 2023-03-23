import requests # http requests
from bs4 import BeautifulSoup # Webscrape
from collections import defaultdict # Default dictionary: store a list with each key
import pandas as pd     # DF

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

url = 'https://www.linkit.nl/vacancies?VacancyType=%5B%22Interim%20opdracht%22%5D'

# Get request to indeed with headers above (you don't need headers!)
response = requests.get(url, headers=headers)
response_json = response.json
html = response.text

# Scrapping the Web (you can use 'html' or 'lxml')
soup = BeautifulSoup(html, 'lxml')

# Outer Most Entry Point of HTML:
outer_most_point=soup.find('div',{'class': 'Overview_overview__2bcF5'})
vacancy_list = outer_most_point.find('div', {'class': 'vacancies_vacancies__reactive-list__3q5G9'})
for i in outer_most_point.find('vacancies_vacancies__vacancy-list__3MhXB'):
    job_title=i.find('h2',{'class':'VacancyCard_vacancy-card__title__1DKYj'})
    print(job_title)

print(html)