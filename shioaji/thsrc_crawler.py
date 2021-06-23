import requests
from bs4 import BeautifulSoup
import mysql.connector


# 台灣高鐵投資人關係頁面
url = "https://www.thsrc.com.tw/ArticleContent/117f6de2-ed8b-403a-ab4a-820d123e37bf"

#使用requests去發送http請求
page = requests.get(url)

#使用html.parser去解析請求回來的網頁
soup = BeautifulSoup(page.text, 'html.parser')

#搜尋定位點html tag為div且class是table_con
first_anchor = soup.find('div', class_='table_con')

#切割\n
data = (first_anchor.text).split('\n')
new_data = []
#資料過濾，排除表頭和空白
for item in data:
    if item == "年度/月份" or item == "旅客人數(人次)" or item == "延人公里(人公里)" :
        pass
    elif  item == "":
        pass
    else:
        new_data.append(item) #將我要的資料重新加載至新的list

#印出
print(new_data)

#連線到資料庫
mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="temp",
    auth_plugin="mysql_native_password"
)

#資料寫入到mysql
for total in new_data: #遞迴所有資料
    if len(new_data) != 0: #如果new_data list的長度不為0
        mycursor = mydb.cursor()
        sql = "INSERT INTO `thsrc`(`date`, `travler`, `km_per_travler`) VALUES (%s, %s, %s)"
        val = str(new_data[0]), str(new_data[1]), str(new_data[2]) #將new_data裡的前三筆資料帶入

        mycursor.execute(sql, val) #mysql執行
        mydb.commit() #mysql生效
        del(new_data[0:3]) #刪除new_data list裡的前三筆
    else: #如果new_data list的長度為0
        break #離開遞迴







