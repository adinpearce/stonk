import mysql.connector
import datetime
from shioaji.data import Ticks
import shioaji as  sj
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

#initialize
api = sj.Shioaji()
#login
account = api.login("S125235872", "adin2427")

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

current = datetime.datetime.strptime(time_combination, "%Y-%m-%d")
D_M1 = current + datetime.timedelta(days=-1)
D_M2 = current + datetime.timedelta(days=-2)
D_M3 = current + datetime.timedelta(days=-3)
D_M4 = current + datetime.timedelta(days=-4)

Date_M1 = str(D_M1.strftime("%Y")) + "-"+str(D_M1.strftime("%m"))+"-"+str(D_M1.strftime("%d"))
Date_M2 = str(D_M2.strftime("%Y")) + "-"+str(D_M2.strftime("%m"))+"-"+str(D_M2.strftime("%d"))
Date_M3 = str(D_M3.strftime("%Y")) + "-"+str(D_M3.strftime("%m"))+"-"+str(D_M3.strftime("%d"))
Date_M4 = str(D_M4.strftime("%Y")) + "-"+str(D_M4.strftime("%m"))+"-"+str(D_M4.strftime("%d"))

Date_array = [time_combination, Date_M1, Date_M2, Date_M3, Date_M4]

query_date = "`date` = '"+time_combination+"' OR `date` = '"+Date_M1+"' OR `date` = '"+Date_M2+"' OR `date` = '"+Date_M3+"' OR `date` = '"+Date_M4+"'"

regex00 = re.compile(r"\d+")

def fetcher(stock_num):
    contracts = [api.Contracts.Stocks[str(stock_num)]]
    snapshots = api.snapshots(contracts)

    close_price = snapshots[0]['close']

    return close_price

def operator_checker(stock_name, OS):
    if OS == "linux":
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    elif OS == "windows":
        browser = webdriver.Chrome(executable_path='C:/Users/retr0/Desktop/chromedriver')

    match = regex00.search(stock_name)
    stock_num = match.group(0)

    url = "http://jsjustweb.jihsun.com.tw/z/zc/zco/zco_"+str(stock_num)+".djhtm"

    browser.get(url)

    time.sleep(1)
    url_content = browser.page_source

    soup = BeautifulSoup(url_content, "html.parser")

    operator_cht_array = ["凱基-台北","元大-土城永寧","富邦-嘉義","美林"]

    include_array = []

    for names in operator_cht_array:
        temp_array = []
        try:
            temp_array.append(names)
            operator_OTG = soup.find_all(text=re.compile(names))

            if names == "美林":
                target = operator_OTG[1].parent.parent.parent
            else:
                target = operator_OTG[0].parent.parent.parent

            target_2 = target.find_all('td')
            
            if target_2[5].text == names:
                continue
            else:
                percentage = target_2[4].text

                percentage = percentage.split('%')

                new_percentage = float(percentage[0])

                temp_array.append(new_percentage)
                include_array.append(temp_array)
        except:
            pass

    return include_array

def fubon_jiangguo_module():
    absolute_array = []
    possible_result_array = []

    fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE  `operator` = 'fubon_jiangguo' AND `date` = '"+str(time_combination)+"' ORDER BY `daily_rank` ASC LIMIT 5"

    mycursor.execute(fetch_sql)

    fetch = mycursor.fetchall()

    for item in fetch:
        stock_name = item[2]
        percentage = float(item[-2])

        if percentage > 5:
            possible_result_array.append(stock_name)

    for item_2 in possible_result_array:
        match = regex00.search(item_2)
        stock_num = match.group(0)

        current_stock_price = fetcher(stock_num)

        status_check = []
        converge_array = operator_checker(item_2, 'windows')
        if len(converge_array) >= 2:
            for operator in converge_array:
                if operator[0] == "凱基-台北":
                    if operator[1] > 4:
                        status_check.append("ok")
                if operator[0] == "美林":
                    status_check.append("ok")
            if current_stock_price < 150:
                status_check.append("ok")
            '''
            if current_stock_price < 100 and current_stock_price > 50:
                status_check.append("perfect")
            '''
            if len(status_check) >= 3:
                absolute_array.append(item_2)
                

    #print(possible_result_array)
    #print(absolute_array)

    sql_insert = "INSERT INTO `bargain_determine_v2`(`date`, `operator`, `possible_result`, `absolute_result`) VALUES (%s, %s, %s, %s)"
    val = time_combination, "fubon_jiangguo", str(possible_result_array), str(absolute_array)

    mycursor.execute(sql_insert, val)
    mydb.commit()


fubon_jiangguo_module()
#print(operator_checker('1722台肥', 'windows'))