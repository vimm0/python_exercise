from bs4 import BeautifulSoup
import requests

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# page.content
# page.status_code
# page.headers['content-type']
# page.encoding
# page.text

# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify)
# # print(list(soup.children))
# # print([type(item) for item in list(soup.children)])

# html = list(soup.children)[2]
# body = list(html.children)[3]
# p = list(body.children)[1]
# print(p.get_text())

# soup.find_all('p')
# soup.find_all('p')[0].get_text()

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup)
# # print(soup.find_all('p', class_='outer-text'))
# print(soup.select("div p"))

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()
# img = tonight.find("img")
# desc = img['title']

# print(desc)
# print(period)
# print(short_desc)
# print(temp)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# print(temps)
# print(descs)

import pandas as pd
weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

print("Mean: ", weather["temp_num"].mean())
