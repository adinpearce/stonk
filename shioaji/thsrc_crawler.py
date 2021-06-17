import requests
from bs4 import BeautifulSoup
import mysql.connector

url = "https://www.thsrc.com.tw/ArticleContent/117f6de2-ed8b-403a-ab4a-820d123e37bf"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

first_anchor = soup.find('div', class_='table_con')

data = (first_anchor.text).split('\n')
new_data = []
for item in data:
    if item == "年度/月份" or item == "旅客人數(人次)" or item == "延人公里(人公里)" :
        pass
    elif  item == "":
        pass
    else:
        new_data.append(item)

print(new_data)

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="temp",
    auth_plugin="mysql_native_password"
)
for total in new_data:
    if len(new_data) != 0:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `thsrc`(`date`, `travler`, `km_per_travler`) VALUES (%s, %s, %s)"
        val = str(new_data[0]), str(new_data[1]), str(new_data[2])

        mycursor.execute(sql, val)
        mydb.commit()
        del(new_data[0:3])
    else:
        break







