import mysql.connector
import datetime

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

current = datetime.datetime.strptime(time_combination, "%Y-%m-%d")
D_M1 = current + datetime.timedelta(days=-1)
D_M2 = current + datetime.timedelta(days=-2)
D_M3 = current + datetime.timedelta(days=-3)
D_M4 = current + datetime.timedelta(days=-4)

Date_M1 = str(D_M1.strftime("%Y")) + "-"+str(D_M1.strftime("%m"))+"-"+str(D_M1.strftime("%d"))
Date_M2 = str(D_M2.strftime("%Y")) + "-"+str(D_M2.strftime("%m"))+"-"+str(D_M2.strftime("%d"))
Date_M3 = str(D_M3.strftime("%Y")) + "-"+str(D_M3.strftime("%m"))+"-"+str(D_M3.strftime("%d"))
Date_M4 = str(D_M4.strftime("%Y")) + "-"+str(D_M4.strftime("%m"))+"-"+str(D_M4.strftime("%d"))

query_date = "`date` = '"+time_combination+"' OR `date` = '"+Date_M1+"' OR `date` = '"+Date_M2+"' OR `date` = '"+Date_M3+"' OR `date` = '"+Date_M4+"'"

def determine(operator, date, query_date):
    sql = "SELECT * FROM `bargain_ticket_data` WHERE `operator` = '"+str(operator)+"' AND `date` = '"+str(date)+"'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for amount in myresult:
        amount_array = [0, 0, 0, 0, 0]
        amount_num = 0
        if operator == "KGI_taipei":
            fetch_sql = "SELECT * FROM `bargain_ticket_data` WHERE `stock_name` = '"+str(amount[2])+"' AND `operator` = '"+str(operator)+"' AND ("+query_date+") ORDER BY `date` ASC"
            mycursor.execute(fetch_sql)

            myresult_fetch = mycursor.fetchall()

            for detail in myresult_fetch:
                amount_transaction = int(detail[5])
                if detail[1] == time_combination:
                    amount_array[0] = amount_transaction
                elif detail[1] == Date_M1:
                    amount_array[1] = amount_transaction
                elif detail[1] == Date_M2:
                    amount_array[2] = amount_transaction
                elif detail[1] == Date_M3:
                    amount_array[3] = amount_transaction
                elif detail[1] == Date_M4:
                    amount_array[4] = amount_transaction
                amount_num += amount_transaction

            try:
                print(str(amount[2])+"==>連買"+str(amount_array.index(0)))
            except:
                print(str(amount[2])+"==>連買5, " +str(amount_num))

            if amount[-1] < 6:
                print(str(amount[2])+"==>放空")
            



determine("KGI_taipei", time_combination, query_date)
