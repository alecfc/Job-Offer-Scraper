from master_scraper import *

class UkomstScraper(MasterScraper):

    url = "https://app.catsone.nl/portal?id=4337"

    payload={}
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'accept': '*/*'
    }
    
    def parse(self):
        data = self.load_json(website='Ukomst')
        for idx, job in enumerate(data['jobs']):
            job_info = {}
            if idx > 25:
                break
            job_info['Job Website'] = 'Ukomst'
            job_info['Date Published'] = job['date_created'].split('T')[0]
            job_info['Title'] = job['title']
            if '(' in job_info['Title']: #and re.match(r"(([a-z])+)([0-9]+)", job_info['Title'], re.I):
                temp_title = job_info['Title']
                job_info['Hours'] = temp_title.split('(')[1].replace(')','').split(' ')[0]
                job_info['Title'] = job_info['Title'].split('(')[0].strip()
            else:
                job_info['Hours'] = 'NA'
            job_info['URL'] = job['url']
            job_info['Company'] = job['custom_fields'][1]['value']
            job_info['Location'] = job['location']['city']
            job_info['Description'] = BeautifulSoup(job['description'], "lxml").text

            job_info['Duration'] = job['duration']
            self.job_list.append(job_info)
        self.save_json(data=self.job_list, website='Ukomst', parsed=True)

temp = UkomstScraper()
temp.scrape('Ukomst')
temp.parse()