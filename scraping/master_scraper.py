import json
import requests
from bs4 import BeautifulSoup

class MasterScraper():
    job_list = []
    url = ''
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    payload = {}
    def save_json(self, data, website, parsed):
        if parsed:
            save_string = 'data/'+website+'_parsed.json'
        else:
            save_string = 'data/'+website+'.json'
        with open(save_string, 'w') as f:
            json.dump(data, f)
    
    def load_json(self, website):
        with open('data/'+website+'.json', 'r') as read_file:
            data = json.load(read_file)
        return data
    
    def scrape(self, website):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        self.save_json(data=response.json(), website=website, parsed=False)
    
    def parse(self):
        return