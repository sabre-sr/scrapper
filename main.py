#!usr/bin/env python3
from selenium import webdriver
import bs4
import os
# launch url
url = 'http://chatbot.admiralbulldog.live/playsound'
os.makedirs("soundboard", exist_ok=True)

# create a browser session with webdriver
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(30)
html_page = driver.page_source
with open("source.html", "w") as file:
    file.write(html_page)
driver.quit()

sounds = bs4.BeautifulSoup(html_page, "lxml")
for link in sounds.find_all('audio'):
    print(link)
