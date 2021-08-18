import mysql.connector
import datetime
from shioaji.data import Ticks
import shioaji as  sj
import re
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

def fetcher(stock_num):
    contracts = [api.Contracts.Stocks[str(stock_num)]]
    snapshots = api.snapshots(contracts)

    close_price = snapshots[0]['close']

    return close_price

def KGI_taipei_module(type, OS):
    if type == "ticket":
        fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE  `operator` = 'KGI_taipei' AND `date` = '2021-08-09' ORDER BY `date` ASC"
        #fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE  `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"' ORDER BY `date` ASC"
    elif type == "money":
        fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = 'KGI_taipei' AND `date` = '2021-08-09' ORDER BY `date` ASC"
        #fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"' ORDER BY `date` ASC"

    if OS == "linux":
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    elif OS == "windows":
        browser = webdriver.Chrome(executable_path='C:/Users/retr0/Desktop/chromedriver')

    mycursor.execute(fetch_sql)

    fetch = mycursor.fetchall()

    stock_num_array = []

    for data in fetch:
        stock_full = data[2]
        regex00 = re.compile(r"\d+")
        match = regex00.search(stock_full)
        stock_num = match.group(0)

        long = len(stock_num)

        if long >= 5:
            pass
        else:
            stock_num_array.append(stock_num)
            #print(data[2])

    for item in stock_num_array:
        url = "http://jsjustweb.jihsun.com.tw/z/zc/zco/zco_"+str(item)+".djhtm"

        browser.get(url)

        time.sleep(1)
        url_content = browser.page_source

        soup = BeautifulSoup(url_content, "html.parser")

        operator_OTG = soup.find_all(text=re.compile("凱基-台北"))

        target = operator_OTG[0].parent.parent.parent

        target_2 = target.find_all('td')

        print(target_2)


    

KGI_taipei_module("ticket", "windows")