"""
program
"""
from bs4 import BeautifulSoup
import requests
GET_URL = 'https://yandex.kz/pogoda/astana'
respons = requests.get(GET_URL)
soup = BeautifulSoup(respons.text,'html.parser')
tmp = soup.find('span',class_='temp__value temp__value_with-unit').text
print(tmp + '°C')
