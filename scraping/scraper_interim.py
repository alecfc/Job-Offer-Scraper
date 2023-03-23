from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://interimprofessionals.hero.eu/interim-opdrachten/'

driver = webdriver.Chrome()
driver.get(url)

job_offers = driver.find_elements(By.CLASS_NAME, 'jet-posts__item')

for job_offer in job_offers[:20]:
    actions = ActionChains(driver)
    actions.click(job_offer).perform()
    title = job_offers[1].find_element(By.CLASS_NAME,'entry-title').text
    print(title)