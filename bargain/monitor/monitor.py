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

now = datetime.datetime.now()
time_combination = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

current = datetime.datetime.strptime(time_combination, "%Y-%m-%d")
D_M1 = current + datetime.timedelta(days=-1)
Date_M1 = str(D_M1.strftime("%Y")) + "-"+str(D_M1.strftime("%m"))+"-"+str(D_M1.strftime("%d"))

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


def stock_num_fetcher(DM1):
    regex00 = re.compile(r"\d+")
    sql = "SELECT * FROM `bargain_determine` WHERE `date` = '"+str(DM1)+"'"
    mycursor.execute(sql)

    data = mycursor.fetchall()

    absolute_result = data[0][3]
    possible_result = data[0][4]

    def str_to_list(str_to_process):
        finish_array = []
        new_str = str_to_process.strip("[")
        new_str = new_str.strip("]")

        split_str = new_str.split(",")

        for item in split_str:
            item = item.strip(" ")
            item = item.strip("'")

            match = regex00.search(item)
            stock_num = match.group(0)

            finish_array.append(stock_num)

        return finish_array

    return str_to_list(absolute_result), str_to_list(possible_result)


#print(fetcher('2330'))

stock_num_data = stock_num_fetcher(Date_M1)

for stock_num in stock_num_data[0]:
    sql_insert = "INSERT INTO `bargain_daily_operation_temp`(`stock_num`, `opertaor`, `last_tick_price`, `trigger_high_price`, `trigger_low_price`, `status`) VALUES ('"+str(stock_num)+"', 'KGI_taipei', 0, 0, 0, '')"
    mycursor.execute(sql_insert)

    mydb.commit()

for i in range(1, 190):
    time_combination_full = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d")) + ";" + str(now.strftime("%H"))+":"+str(now.strftime("%M"))
    current_time = str(now.strftime("%H"))+":"+str(now.strftime("%M"))

    print("current time==>" + current_time)
    
    if current_time == "09:00":
        for stock_num in stock_num_data[0]:
            current_close_price = fetcher(stock_num)
            high_price, low_price = pawn_calc.calc(current_close_price)

            sql_insert = "INSERT INTO `bargain_daily_operation_temp`(`stock_num`, `opertaor`, `last_tick_price`, `trigger_high_price`, `trigger_low_price`, `status`) VALUES ('"+str(stock_num)+"', 'KGI_taipei', '"+str(current_close_price)+"','"+str(high_price)+"','"+str(low_price)+"', '')"
            sql_update = "UPDATE `bargain_daily_operation_temp` SET `last_tick_price`='"+str(current_close_price)+"', `trigger_high_price` = '"+str(high_price)+"', `trigger_low_price`== '"+str(low_price)+"', `status`= '--' WHERE `stock_num` = '"+str(stock_num)+"'"
            mycursor.execute(sql_insert)

            mydb.commit()
    elif current_time == "09:05":
        for stock_num in stock_num_data[0]:
            current_close_price = fetcher(stock_num)

            update_sql = "UPDATE `bargain_daily_operation_temp` SET `last_tick_price`='"+str(current_close_price)+"', `status`= 'hold' WHERE `stock_num` = '"+str(stock_num)+"'"
            mycursor.execute(update_sql)

            mydb.commit()

            insert_sql = "INSERT INTO `bargain_operation_result`(`buy_date`, `sell_date`, `stock_name`, `buy_price`, `sell_price`, `amount`, `result`, `operator`, `bid`, `type`) VALUES ('"+str(time_combination_full)+"','','"+str(stock_num)+"','','"+str(current_close_price)+"','1000','','KGI_taipei','0','')"
            mycursor.execute(sql_insert)

            mydb.commit()
    else:
        for stock_num in stock_num_data[0]:
            current_close_price = fetcher(stock_num)
            select_sql = "SELECT * FROM `bargain_daily_operation_temp` WHERE `stock_num` = '"+str(stock_num)+"'"
            mycursor.execute(select_sql)

            data = mycursor.fetchall()

            update_sql = "UPDATE `bargain_daily_operation_temp` SET `last_tick_price`='"+str(current_close_price)+"', `status`= 'hold' WHERE `stock_num` = '"+str(stock_num)+"'"
            mycursor.execute(update_sql)

            mydb.commit()

            trigger_high_price = data[0][4]
            trigger_low_price = data[0][5]

            if float(current_close_price) > float(trigger_high_price):
                update_sql = "UPDATE `bargain_daily_operation_temp` SET `status`= 'sold_negative' WHERE `stock_num` = '"+str(stock_num)+"'"
                mycursor.execute(update_sql)

                mydb.commit()

                update_sql = "UPDATE `bargain_operation_result` SET `sell_date`='"+str(time_combination_full)+"',`buy_price`='"+str(current_close_price)+"' WHERE `stock_name` LIKE '"+str(stock_num)+"%' AND `buy_date` LIKE '"+str(time_combination)+"%'"
                mycursor.execute(update_sql)

                mydb.commit()
            elif float(current_close_price) < float(trigger_low_price):
                update_sql = "UPDATE `bargain_daily_operation_temp` SET `status`= 'sold_positive' WHERE `stock_num` = '"+str(stock_num)+"'"
                mycursor.execute(update_sql)

                mydb.commit()

                update_sql = "UPDATE `bargain_operation_result` SET `sell_date`='"+str(time_combination_full)+"',`buy_price`='"+current_close_price+"' WHERE `stock_name` LIKE '"+str(stock_num)+"%' AND `buy_date` LIKE '"+str(time_combination)+"%'"
                mycursor.execute(update_sql)

                mydb.commit()
    time.sleep(60)





