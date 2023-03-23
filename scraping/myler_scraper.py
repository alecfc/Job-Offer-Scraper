from master_scraper import *

class MylerScraper(MasterScraper):
    url = "https://www.myler.nl/opdrachten/"

    payload={}
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Cookie': 'uncode_privacy[consent_types]=%5B%5D',
            'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    def parse(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        html = response.text

        # Scrapping the Web (you can use 'html' or 'lxml')
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find_all(attrs={'class':'col-md-4'})
        for job in jobs:
            job_info = {}
            job_info['URL'] = job.find('a')['href']
            # Get response from job page and read HTML
            job_response = requests.request("GET", job_info['URL'], headers=self.headers, data=self.payload)
            job_soup = BeautifulSoup(job_response.text, "html.parser")

            # Extract Information
            job_items = job_soup.find_all(attrs={'class':'hfp_item'})
            job_info['Employer'] = job_soup.find(attrs={'class':'d-flex align-items-center flex-md-column'}).text.replace('\n','')
            job_info['Title'] = job_items[0].text.split('\n')[2]
            job_info['Location'] = job_items[1].text.split('\n')[2]
            job_info['Hours per Week'] = job_items[2].text.split('\n')[2]
            job_info['Job Duration'] = job_items[3].text.split('\n')[2].replace(' ','')
            job_info['Job Description'] = job_soup.find(attrs={'class':'hfp_read-more'}).text
            self.job_list.append(job_info)
        
        self.save_json(data=self.job_list, website='Myler', parsed=True)

