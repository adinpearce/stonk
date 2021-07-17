from os import sep
import mysql.connector
import datetime
import re
import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

#browser = webdriver.Chrome(executable_path='C:/Users/retr0/Desktop/chromedriver')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

#凱基-台北
url_KGI_taipei = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=E&d=1" 

browser.get(url_KGI_taipei)

url_content = browser.page_source

soup = BeautifulSoup(url_content, "html.parser")

first_anchor = soup.find_all(class_='t0')

buy_over = first_anchor[1].text
phase1 = buy_over.split('\n')

new_array = []

for item in phase1:
    if item != "":
        new_array.append(item)

print(new_array[5:])

