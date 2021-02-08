from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")

import requests
import os, time, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import urllib.request

search_word = "橋本環奈"
download_num = 100
start = 1

# launch chrome browser
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options = options)

for i in range(start,download_num+start):
    driver.get("https://search.yahoo.co.jp/image/search?p=" + search_word + "&ei=UTF-8&b=" + str(i))
    elem = driver.find_element_by_css_selector("#contentsInner > div > section > section:nth-child(6) > div > div:nth-child(1) > div:nth-child(1) > figure > a > img")
    photo_url = elem.get_attribute("src")
    file_name = str(i) + "_" + search_word
    urllib.request.urlretrieve(photo_url,"{}.jpeg".format(file_name))
    time.sleep(5)

driver.quit()
