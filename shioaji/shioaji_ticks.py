
from shioaji.data import Ticks
import shioaji as  sj
import pandas as pd
import mysql.connector
import datetime
import kd_api



#initialize
api = sj.Shioaji()

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

now = datetime.datetime.now()
today_date = str(now.strftime("%Y"))+"-" + \
        str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

#login
account = api.login("S125235872", "adin2427")

stonk_list = [2302, 2303, 2329, 2330, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]


for data in stonk_list:
    contracts = [api.Contracts.Stocks[str(data)]]
    snapshots = api.snapshots(contracts)

    stonk_code = snapshots[0]['code']
    high = snapshots[0]['high']
    low = snapshots[0]['low']
    open_price = snapshots[0]['open']
    close_price = snapshots[0]['close']
    avg_price = snapshots[0]['average_price']
    total_volume = snapshots[0]['total_volume']
    '''
    print("high: " + str(high))
    print("low: " + str(low))
    print("open_prices: " + str(open_price))
    print("close: " +str(close_price))
    print("avg_prices: " +str(avg_price))
    print("total_volume: " + str(total_volume))
    print("fetch success" + "="*50)
    '''
    try:
        sql = "INSERT INTO `" + str(stonk_code) + "`(`date`, `open`, `close`, `high`, `low`, `avg_price`, `volume`, `k`, `d`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = today_date, open_price, close_price, high, low, avg_price, total_volume, "", ""
        mycursor.execute(sql, val)
        mydb.commit()
        final_stat = kd_api.kd_counter(data, "yes")
        print(str(stonk_code)+ "==>success")
    except Exception as db_error:
        print(db_error)


