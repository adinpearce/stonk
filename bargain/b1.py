import datetime
from os import close
import requests
import mysql.connector
from bs4 import BeautifulSoup

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

#凱基-台北
url_KGI_taipei = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9200&b=9268" 

response = requests.get(url_KGI_taipei)

soup = BeautifulSoup(response.text, "html.parser")

first_anchor = soup.find_all('table')

print(first_anchor[1])
'''
for item in first_anchor:
    print(item.text)
'''