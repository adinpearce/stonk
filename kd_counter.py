import talib
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

sql = "SELECT `open`, `close`, `high`, `low`, `k`, `d` FROM `2330` ORDER BY `date` DESC LIMIT 9"
mycursor.execute(sql)
myresult = mycursor.fetchall()

open_list = []
high_list = []
low_list = []
close_list = []
k_list = []
d_list = []
total_array = []

for element in myresult:
    open_list.append(element[0])
    close_list.append(element[1])
    high_list.append(element[2])
    low_list.append(element[3])
    k_list.append(element[4])
    d_list.append(element[5])


def data_reconfig(list, type):
    content_array = []
    if type == "standard":
        for data in list:
            data = float(data)
            content_array.append(data)
            total_array.append(data)
    elif type == "k" or type == "d":
        for data in list:
            if data == "":
                pass
            else:
                data = float(data)
                content_array.append(data)

    return content_array


open_array = data_reconfig(open_list, "standard")
close_array = data_reconfig(close_list, "standard")
high_array = data_reconfig(high_list, "standard")
low_array = data_reconfig(low_list, "standard")
k_array = data_reconfig(k_list, "k")
d_array = data_reconfig(d_list, "d")

biggest = max(total_array)
smallest = min(total_array)

today_close = close_array[0]

rsv = round((today_close - smallest) / (biggest - smallest) * 100, 2)

yesterday_k = k_array[0]

k = round((yesterday_k / 3 * 2) + (rsv / 3), 2)

yesterday_d = d_array[0]

d = round((k / 3)+(yesterday_d/3*2), 2)
print(d)
