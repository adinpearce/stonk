import mysql.connector
import datetime
import re

now = datetime.datetime.now()

date_time =  str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))
time_combination = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))+";"+str(now.strftime("%H"))+":"+str(now.strftime("%M"))

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="retr0",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

def list_to_str(data):
    if data == '[]' :
        empty_array = []
    else:
        empty_array = []
        data = str(data).strip("[")
        data = data.strip("]")
        data_array = data.split(',')
        for item in data_array:
            item = item.strip(" ")
            item = item.strip("'")
            empty_array.append(item)

    return empty_array




def center(data, userID, reply_token):
    reply_message = ""
    extra_message = ""
    if data == "今日操作":
        sql = "SELECT * FROM `bargain_determine_v2` ORDER BY `date` DESC LIMIT 2"
        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for item in myresult:
            ref_date = item[1]
            operator = item[2]
            absolute_result = item[3]

            absolute_result_modify = ""
            absolute_result_show = list_to_str(absolute_result)
            if absolute_result_show == []:
                absolute_result_modify = "\n因為該券商昨天在混，所以沒有標的"
            else:
                for insider in absolute_result_show:
                    if absolute_result_modify == "":
                        absolute_result_modify = "\n" + insider
                    else:
                        absolute_result_modify = absolute_result_modify + "\n" + insider

            if operator == "KGI_taipei":
                ref_operator = "凱基-台北"
            elif operator == "fubon_jiangguo":
                ref_operator = "富邦-建國"

            temp_reply_message = "參考日期: " + str(ref_date) + "\n分點: " + str(ref_operator) + "\n放空標的: " + str(absolute_result_modify)
        
            if reply_message != "":
                reply_message = reply_message + "\n\n" + temp_reply_message
            else:
                reply_message = temp_reply_message
    elif data == "操作法則":
        '''
        2021-08-02操作規則:
        1.鎖定隔日沖買超12%的股票
        2.停利設定2%、停損設定2%
            2.1==>10:00停損設定為5%
            2.2==>11:00停利設定為1%
            2.3==>如當天大盤明顯較強，停利設定為1.5%
        3.11:30為強制買回時間
        4.不交易超過150元之股票
        '''
        current_hr = int(now.strftime("%H"))
        current_ms = int(now.strftime("%M"))

        special_status = "off"

        if special_status == "off":
            if current_hr == 12:
                if current_ms > 30:
                    operation_rule = "強制停利/停損"
                elif current_ms == 30 or current_ms > 30:
                    operation_rule = "1.停利點設定:1%\n2.停損點設定:2%"
            elif current_hr > 12:
                operation_rule = "強制停利/停損"
            elif current_hr == 11 or current_hr > 11:
                operation_rule = "1.停利點設定:1%\n2.停損點設定:2%"
            elif current_hr == 10 or current_hr > 10:
                operation_rule = "1.停利點設定:2%\n2.停損點設定:2%"
            elif str(current_hr) == '09' or str(current_hr) > '09':
                operation_rule = "1.09:05放空\n2.停利點設定:2%\n3.停損點設定:漲停前兩檔"

            reply_message = operation_rule
        elif data == "指令":
            reply_message = "今日操作:列出所有今日資料來源券商、操作方式、操作方向\n\n操作法則:列出在該時間持股停損、停利狀態\n\n紀錄:開始手動紀錄回測紀錄"
        elif data == "紀錄":
            reply_message = ""   


    return reply_message, extra_message


print(center("今日操作", "", ""))
