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

def fetcher(OS, url):
    if OS == "linux":
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    elif OS == "windows":
        browser = webdriver.Chrome(executable_path='C:/Users/retr0/Desktop/chromedriver')

    browser.get(url)

    url_content = browser.page_source

    soup = BeautifulSoup(url_content, "html.parser")

    first_anchor = soup.find_all(class_='t0')

    buy_over = first_anchor[1].text
    phase1 = buy_over.split('\n')

    new_array = []

    for item in phase1:
        if item != "":
            new_array.append(item)

    browser.close()

    return new_array[5:]