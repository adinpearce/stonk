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

sql = "SELECT high, low , close FROM `2330` WHERE 1"
mycursor.execute(sql)
myresult = mycursor.fetchall()

high_list = []
low_list = []
close_list = []

for element in myresult:
    high_list.append(element[0])
    low_list.append(element[1])
    close_list.append(element[2])


def list_type_changer(list):
    content_array = []
    for data in list:
        data = float(data)
        content_array.append(data)

    return content_array


high_list = list_type_changer(high_list)
low_list = list_type_changer(low_list)
close_list = list_type_changer(close_list)

high_array = np.asarray(high_list)
low_array = np.asarray(low_list)
close_array = np.asarray(close_list)

k, d = talib.STOCH(high_array, low_array, close_array, fastk_period=5,
                   slowk_period=3, slowk_matype=1, slowd_period=3, slowd_matype=1)
#k, d = talib.STOCHF(high_array, low_array, close_array,fastk_period=9, fastd_period=3, fastd_matype=3)

#print(k, d)

for element1 in k:
    if element1 != "nan":
        print(element1)
