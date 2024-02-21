from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.nash-gorod.kz/ru/0/3/WeatherAndRate')
Rate = driver.find_element(By.CSS_SELECTOR, '.vert-row .caption')
print (Rate.text)
