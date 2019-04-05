from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get('https://weather.com/en-IN/weather/tenday/l/INXX0038:1:IN')
soup = BeautifulSoup(page.content, 'html.parser')
weatherReport = soup.find(id='twc-scrollabe')
items = weatherReport.find_all(class_='clickable closed')
dates = [item.find(class_='day-detail clearfix').get_text() for item in items]
descriptions = [item.find(class_='description').get_text() for item in items]
temperatures = [] 
for item in items:
  item = item.find(class_='temp')
  spans = item.find_all('span')
  temp = ''
  for span in spans:
    if not temp:
      temp = span.get_text()+'/'
    else:
      temp+=span.get_text()
  temperatures.append(temp)

weather_stuff = pd.DataFrame({
  'date':dates,
  'description':descriptions,
  'temperatures (MAX/MIN)':temperatures
})
weather_stuff.to_csv('result.csv')