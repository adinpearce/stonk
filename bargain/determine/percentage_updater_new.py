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

def percentage_updater(OS, url, operator):
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

    time.sleep(1)
    url_content = browser.page_source

    soup = BeautifulSoup(url_content, "html.parser")

    if operator == "KGI_taipei":
        operator_name = '凱基-台北'
    elif operator == "yuanta_tucheng":
        operator_name = '元大-土城永寧'
    elif operator == "fubon_jiangguo":
        operator_name = '富邦-建國'
    elif operator == "fubon_chiayi":
        operator_name = '富邦-嘉義'
    elif operator == "lynch":
        operator_name = '美林'

    try:
        operator_OTG = soup.find_all(text=re.compile(operator_name))
        
        if operator_name == "美林":
            target = operator_OTG[1].parent.parent.parent
        else:
            target = operator_OTG[0].parent.parent.parent

        target_2 = target.find_all('td')

        percentage = target_2[4].text

        percentage = percentage.split('%')

        new_percentage = float(percentage[0])
    except:
        new_percentage = 0

    browser.close()
    return new_percentage



def main_host(date, type):
    if type == "ticket":
        fetch = "SELECT * FROM `bargain_ticket_data` WHERE `date` = '"+str(date)+"'"
    elif type == "money":
        fetch = "SELECT * FROM `bargain_money_data` WHERE `date` = '"+str(date)+"'"
    mycursor.execute(fetch)

    myresult = mycursor.fetchall()

    regex00 = re.compile(r"\d+")


    for amount in myresult:
        time.sleep(1)
        org_stock_name = str(amount[2])
        operator = str(amount[6])

        print("正在蒐集"+str(operator)+"對"+str(org_stock_name))
        
        match = regex00.search(org_stock_name)

        try:
            stock_num = match.group(0)

            url_generate = "http://jsjustweb.jihsun.com.tw/z/zc/zco/zco.djhtm?a="+stock_num

            percentage = percentage_updater('windows', url_generate, operator)

            print("比率="+str(percentage)+"%")

            if type == "ticket":
                update_sql = "UPDATE `bargain_ticket_data` SET `percentage` = '"+str(percentage)+"' WHERE `date` = '" + date + "' AND `stock_name` = '" + org_stock_name +"' AND `operator` = '"+str(operator)+"'"
                print("已完成更新bargain_ticket_data")
            elif type == "money":
                update_sql = "UPDATE `bargain_money_data` SET `percentage` = '"+str(percentage)+"' WHERE `date` = '" + date + "' AND `stock_name` = '" + org_stock_name +"' AND `operator` = '"+str(operator)+"'"
                print("已完成更新bargain_money_data")

            mycursor.execute(update_sql)

            mydb.commit()

            print("="*75)
        except Exception as error:
            print(error)
            continue


main_host(time_combination, 'money')
main_host(time_combination, 'ticket')
