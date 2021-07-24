import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

current = datetime.datetime.strptime(time_combination, "%Y-%m-%d")
D_M1 = current + datetime.timedelta(days=-1)
D_M2 = current + datetime.timedelta(days=-2)
D_M3 = current + datetime.timedelta(days=-3)
D_M4 = current + datetime.timedelta(days=-4)

Date_M1 = str(D_M1.strftime("%Y")) + "-"+str(D_M1.strftime("%m"))+"-"+str(D_M1.strftime("%d"))
Date_M2 = str(D_M2.strftime("%Y")) + "-"+str(D_M2.strftime("%m"))+"-"+str(D_M2.strftime("%d"))
Date_M3 = str(D_M3.strftime("%Y")) + "-"+str(D_M3.strftime("%m"))+"-"+str(D_M3.strftime("%d"))
Date_M4 = str(D_M4.strftime("%Y")) + "-"+str(D_M4.strftime("%m"))+"-"+str(D_M4.strftime("%d"))

Date_array = [time_combination, Date_M1, Date_M2, Date_M3, Date_M4]

query_date = "`date` = '"+time_combination+"' OR `date` = '"+Date_M1+"' OR `date` = '"+Date_M2+"' OR `date` = '"+Date_M3+"' OR `date` = '"+Date_M4+"'"

def KGI_taipei_module(type):
    absolute_array = []
    possible_result_array = []
    buy_in_status = []
    if type == "ticket":
        #fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE  `operator` = 'KGI_taipei' AND `date` = '2021-07-21' ORDER BY `date` ASC"
        fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE  `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"' ORDER BY `date` ASC"
    elif type == "money":
        #fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = 'KGI_taipei' AND `date` = '2021-07-21' ORDER BY `date` ASC"
        fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"' ORDER BY `date` ASC"

    mycursor.execute(fetch_sql)

    fetch = mycursor.fetchall()

    for item in fetch:
        stock_name = item[2]
        percentage = float(item[-2])

        if percentage > 5:
            possible_result_array.append(stock_name)


    for item_2 in possible_result_array:
        if type == "money":
            new_fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE `stock_name` = '"+item_2+"' AND `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"'"
            #new_fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE `stock_name` = '"+item_2+"' AND `operator` = 'KGI_taipei' AND `date` = '2021-07-21'"
        elif type == "ticket":
            new_fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `stock_name` = '"+item_2+"' AND  `operator` = 'KGI_taipei' AND `date` = '"+time_combination+"'"
            #new_fetch_sql = "SELECT * FROM `bargain_money_data` WHERE `stock_name` = '"+item_2+"' AND  `operator` = 'KGI_taipei' AND `date` = '2021-07-21'"

        mycursor.execute(new_fetch_sql)

        new_fetch_data = mycursor.fetchall()

        if len(new_fetch_data) != 0:
            absolute_array.append(item_2)
            #possible_result_array.remove(item_2)

    print(possible_result_array)
    print(absolute_array)
    
    if type == "ticket":
        sql_insert = "INSERT INTO `bargain_determine`(`date`, `operator`, `possible_result`, `absolute_result`) VALUES (%s, %s, %s, %s)"
        val = time_combination, "KGI_taipei", str(possible_result_array), str(absolute_array)

        mycursor.execute(sql_insert, val)
        mydb.commit()
    elif type == "money":
        sql_select = "SELECT `possible_result` FROM `bargain_determine` WHERE `date` = '"+time_combination+"'"

        mycursor.execute(sql_select)

        selected_data = mycursor.fetchall()

        data = selected_data[0][0]

        modify_data = '"'+ str(data)+"@"+str(possible_result_array)+'"'

        sql_update = "UPDATE `bargain_determine` SET `possible_result`= "+str(modify_data)+" WHERE `date` = '"+time_combination+"'"

        mycursor.execute(sql_update)

        mydb.commit()

#KGI_taipei_module('ticket')
