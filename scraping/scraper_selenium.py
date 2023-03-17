from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.linkit.nl/vacancies?VacancyType=%5B%22Interim%20opdracht%22%5D'

driver = webdriver.Chrome()
driver.get(url)

job_offers = driver.find_elements(By.CLASS_NAME, 'vacancies_vacancies__vacancy-item__22BIq')

for job_offer in job_offers:
    job_title = job_offers[1].find_element(By.XPATH,'//*[@id="__next"]/div[4]/div/div[2]/div[3]/div/div[2]/div[1]/a/div/div/h3').text
    job_link = job_offer.find_element(By.XPATH,'//*[@id="__next"]/div[4]/div/div[2]/div[3]/div/div[2]/div[1]/a').get_attribute('href')
    job_description = job_offer.find_element(By.XPATH,'//*[@id="__next"]/div[4]/div/div[2]/div[3]/div/div[2]/div[2]/a/div/div/p').text
    job_location = job_offer.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div/div[2]/div[3]/div/div[2]/div[2]/a/footer/div/div[1]/span').text
    job_experience = job_offer.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div/div[2]/div[3]/div/div[2]/div[2]/a/footer/div/div[2]/span').text
    print(job_title,job_description,job_link)