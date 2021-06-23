import mysql.connector
import datetime
import shioaji as  sj
import pandas as pd


#api_initialize
api = sj.Shioaji()
account = api.login("S125235872", "adin2427")

#sql_initialize
mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

#datetime_initialize
now = datetime.datetime.now()
today_date = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

today_date_datetime = datetime.datetime.strptime(today_date, "%Y-%m-%d")


def str_to_list(word):
    new_array = []
    word = str(word).strip("]")
    word = word.strip("[")
    word_array = word.split(",")

    for data in word_array:
        data = data.strip(" ")
        data = data.strip('"')
        data = data.strip("'")
        new_array.append(data)

    return new_array

sql = "SELECT * FROM `semi_kd_determine` ORDER BY `date` DESC LIMIT 30"

mycursor.execute(sql)
myresult = mycursor.fetchall()

verify_date = ['4','3','5','10','20','30']

for data in myresult:
    correct = 0
    opposite = 0
    verify_result = []
    date = data[0]
    stock_list =data[1]
    status_prediction = data[2]
    volume = data[3]
    volume_status = data[4]
    '''
    volume_status_process = str(volume_status).strip("[")
    volume_status_process = volume_status_process.strip("]")

    volume_status_array = volume_status_process.split("], [")

    print(volume_status_array[0])
    '''
    establish_date_datetime = datetime.datetime.strptime(date, "%Y-%m-%d")

    conflict_time = today_date_datetime - establish_date_datetime
    conflict_time_modify = (str(conflict_time).split(" days, 0:00:00"))[0]

    stock_process_list = str_to_list(stock_list)
    status_prediction_process_list = str_to_list(status_prediction)

    if conflict_time_modify in verify_date:
        for count in range(len(stock_process_list)):
            stock_price_1 = str(stock_process_list[count]).strip(" ") #原本的股價
            status_prediction_1 = str(status_prediction_process_list[count]).strip(" ") #原本預測狀態

            contracts = [api.Contracts.Stocks[stock_price_1]]
            snapshots = api.snapshots(contracts)

            stonk_code = snapshots[0]['code']
            close_price = snapshots[0]['close']

            sql_fetch_price = "SELECT * FROM `"+str(stock_process_list[count])+"` WHERE `date` = '" +str(date)+"'"
            mycursor.execute(sql_fetch_price)
            price_result_org_data = mycursor.fetchall()

            price_result = price_result_org_data[0][2]

            if (float(close_price) - float(price_result)) > 0: #如今日股價-該日股價 > 0時(表漲)
                if status_prediction_1 == '0': #如當初判定為死亡交叉
                    print(str(stonk_code) + "==>opposite")  #錯誤預判
                    verify_result.append("error")
                    opposite += 1 
                elif status_prediction_1 == '1': #如當初判定為黃金交叉
                    print(str(stonk_code) + "==>correct")  #正確預判
                    verify_result.append("ok")
                    correct += 1
            elif (float(close_price) - float(price_result)) < 0: #如今日股價-該日股價 < 0時(表跌)
                if status_prediction_1 == '0': #如當初判定為死亡交叉
                    print(str(stonk_code) + "==>correct")  #正確預判
                    verify_result.append("ok")
                    correct += 1
                elif status_prediction_1 == '1': #如當初判定為黃金交叉
                    print(str(stonk_code) + "==>opposite")  #錯誤預判
                    verify_result.append("error")
                    opposite += 1 
            elif (float(close_price) - float(price_result)) == 0: #如今日股價-該日股價 = 0時(表無動)
                if status_prediction_1 == '0': #如當初判定為死亡交叉
                    print(str(stonk_code) + "==>static")  #無預判
                elif status_prediction_1 == '1': #如當初判定為黃金交叉
                    print(str(stonk_code) + "==>static")  #無預判
    else :
        print(date + "非檢核日")

    print("資料日期: " + str(date))
    print("總數為: " + str(len(stock_process_list)))
    print("正確預測筆數:" + str(correct))
    print("錯誤預測筆數:" + str(opposite))
    print("準確率:" + str(round(correct / len(stock_process_list), 2)))
    print("="*50)

    orginal_prediction = str(stock_list) + "@" + str(status_prediction)
    
    if conflict_time_modify == '3' :
        sql = "INSERT INTO `semi_kd_backtrack`(`date`, `original_prediction`, `3day_result`, `5day_result`, `10day_result`, `20day_result`, `30day_result`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = str(date), orginal_prediction, str(verify_result), "", "", "", ""
    elif conflict_time_modify == '5':
        sql = 'UPDATE `semi_kd_backtrack` SET `5day_result` = "'+str(verify_result)+'" WHERE `date` = "' + str(date)+'"'
    elif conflict_time_modify == '10':
        sql = 'UPDATE `semi_kd_backtrack` SET `10day_result` = "'+str(verify_result)+'" WHERE `date` = "' + str(date)+'"'
    elif conflict_time_modify == '20':
        sql = 'UPDATE `semi_kd_backtrack` SET `20day_result` = "'+str(verify_result)+'" WHERE `date` = "' + str(date)+'"'
    elif conflict_time_modify == '30':
        sql = 'UPDATE `semi_kd_backtrack` SET `30day_result` = "'+str(verify_result)+'" WHERE `date` = "' + str(date)+'"'

    if conflict_time_modify == '3':
        mycursor.execute(sql, val)
        mydb.commit()
    elif conflict_time_modify == '5' or conflict_time_modify == '10' or conflict_time_modify == '20' or conflict_time_modify == '30':
        mycursor.execute(sql)
        mydb.commit()








