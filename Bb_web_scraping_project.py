import requests
from bs4 import BeautifulSoup
# copy the forecast url
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YPUvJugzbIU")
# creating object out of  that page
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast")
# print(week)
items = week.find_all(class_="tombstone-container")
print(items[0])
