import time
import mysql.connector
import datetime
from shioaji.data import Ticks
import shioaji as  sj
import re
import pawn_calc

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

def fetcher(stock_num):
    contracts = [api.Contracts.Stocks[str(stock_num)]]
    snapshots = api.snapshots(contracts)

    stonk_code = snapshots[0]['code']
    high = snapshots[0]['high']
    low = snapshots[0]['low']
    open_price = snapshots[0]['open']
    close_price = snapshots[0]['close']
    avg_price = snapshots[0]['average_price']
    total_volume = snapshots[0]['total_volume']

    return close_price


def counter():
    sql = "SELECT * FROM `bargain_daily_operation_temp`"

    mycursor.execute(sql)

    data_fetched = mycursor.fetchall()

    regex00 = re.compile(r"\d+")

    stock_num_array = []

    for data in data_fetched:
        stock_name = data[1]
        match = regex00.search(stock_name)
        stock_num = match.group(0)
        stock_num_array.append(stock_num)

    return stock_num_array

for i in range(1, 190):
    now = datetime.datetime.now()
    time_combination_full = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d")) + ";" + str(now.strftime("%H"))+":"+str(now.strftime("%M"))
    current_time = str(now.strftime("%H"))+":"+str(now.strftime("%M"))

    if current_time == "09:00":
        stock_num_array = counter()
    elif current_time == "09:05":
        for stock_num_item in stock_num_array:
            current_close_price = fetcher(stock_num_item)
            high_price, low_price = pawn_calc.calc(current_close_price)

            sql_update = "UPDATE `bargain_daily_operation_temp` SET `last_tick_price`=%s,`trigger_high_price`=%s,`trigger_low_price`=%s,`update_time`=%s,`status`='starting' WHERE `stock_num` = '"+str(stock_num_item)+"'"
            val = current_close_price, float(high_price), float(low_price), str(time_combination_full)