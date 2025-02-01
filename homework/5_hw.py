from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service()
driver = webdriver.Firefox()
driver.get("https://saucedemo.com/")

try:
    text_user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    text_password = driver.find_element(By.CSS_SELECTOR, '#password')
    button = driver.find_element(By.CSS_SELECTOR, '#login-button')

except:
    print('Elements not found')

else:
    print("Elements found")
