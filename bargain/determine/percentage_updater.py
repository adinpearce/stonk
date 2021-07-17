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

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

def percentage_updater(OS, url):
    if OS == "linux":
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    elif OS == "windows":
        browser = webdriver.Chrome(executable_path='C:/Users/retr0/Desktop/chromedriver')

    browser.get("https://histock.tw/")

    browser.find_element(By.ID, "login").click()
    browser.find_element(By.ID, "email").click()
    browser.find_element(By.ID, "email").send_keys("jona9639@gmail.com")
    time.sleep(1)
    browser.find_element(By.ID, "password").click()
    browser.find_element(By.ID, "password").send_keys("jona789521456")
    time.sleep(1)
    browser.find_element(By.ID, "bLogin").click()

    browser.get(url)
    time.sleep(1)
    url_content = browser.page_source

    soup = BeautifulSoup(url_content, "html.parser")

    first_anchor = soup.find_all(class_='alt-row')

    total_data = first_anchor[0]
    second_anchor = total_data.find_all('td')

    percentage = second_anchor[8].text

    percentage = percentage.split('%')

    new_percentage = float(percentage[0])

    browser.close()

    return new_percentage
    
def main_host(date):
    fetch = "SELECT * FROM `bargain_ticket_data` WHERE `date` = '"+str(date)+"'"
    mycursor.execute(fetch)

    myresult = mycursor.fetchall()

    regex00 = re.compile(r"\d+")

    for amount in myresult:
        org_stock_name = str(amount[2])
        operator = str(amount[6])
        operator_num = 0
        match = regex00.search(org_stock_name)

        stock_num = match.group(0)

        if operator == "KGI_taipei":
            operator_num = 9268

        url_generate = "https://histock.tw/stock/brokertrace.aspx?bno="+str(operator_num)+"&no="+str(stock_num)

        percentage = percentage_updater('windows', url_generate)

        update_sql = "UPDATE `bargain_ticket_data` SET `percentage` = '"+str(percentage)+"' WHERE `date` = '" + date + "' AND `stock_name` = '" + org_stock_name +"'"

        mycursor.execute(update_sql)

        mydb.commit()

main_host(time_combination)
