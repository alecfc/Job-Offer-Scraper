from master_scraper import *


class LINKITScraper(MasterScraper):
    name = 'LINKIT Scraper'
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

    def scrape(self):
        response = requests.request(
            "POST", self.url, headers=self.headers, data=self.payload)
        data = response.json()

        self.save_json(data=data,website='LINKIT',parsed=False)
    
    def parse(self):
        data = self.load_json(website='LINKIT')
        for idx, job in enumerate(data['responses'][0]['hits']['hits']):
            job_info = {}
            if idx > 25:
                break
            job = job['_source']
            job_info['Title'] = job['job_title_nl']
            job_info['URL'] = 'https://www.linkit.nl/vacancies/{}?vacancyType=Interim%20opdracht'.format(
                job['slug_nl'])
            job_info['Company'] = job['client']['name']
            job_info['Location'] = job['location']
            job_info['Description'] = job['function_description_nl']
            job_info['Hours'] = job['hours_per_week']
            job_info['Duration'] = job['duration_in_months']
            job_info['Experience Level'] = job['experience_level']
            self.job_list.append(job_info)
        self.save_json(data=self.job_list, website='LINKIT',parsed=True)