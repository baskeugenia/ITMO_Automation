from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service()
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service = service, options = options)
driver = webdriver.Firefox()
driver.get("https://demoqa.com/")


icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
print('+' if icon is not None else '-')

span = driver.find_element(By.CSS_SELECTOR, 'html body div#app >footer  > span')
print('success' if span is not None else '*')
