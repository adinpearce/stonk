import requests
from bs4 import BeautifulSoup
import mysql.connector

url = "https://www.thsrc.com.tw/ArticleContent/117f6de2-ed8b-403a-ab4a-820d123e37bf"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

first_anchor = soup.find_all('div', class_='table_con')
second_anchor = first_anchor[3]
data = (second_anchor.text).split('\n')
new_data = []
for item in data:
    if item == "年度/月份" or item == "座位利用率" or item == "列車準點率" or item == "列車發車率":
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
        sql = "INSERT INTO `thsrc_2`(`date`, `seat_available`, `train_on_time`, `train_depart`) VALUES (%s, %s, %s, %s)"
        val = str(new_data[0]), str(new_data[1]), str(new_data[2]), str(new_data[3])

        mycursor.execute(sql, val)
        mydb.commit()
        del(new_data[0:4])
    else:
        break







