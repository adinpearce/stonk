import mysql.connector
import datetime
import KGI_taipei_determine as KGI_determine
#import Lynch_determine 

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

def determine(operator, date, query_date, type):
    if type == "ticket":
        sql = "SELECT * FROM `bargain_ticket_data` WHERE `operator` = '"+str(operator)+"' AND `date` = '"+str(date)+"'"
        #sql = "SELECT * FROM `bargain_ticket_data` WHERE `operator` = '"+str(operator)+"' AND `date` = '2021-07-21'"
    elif type == "money":
        sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = '"+str(operator)+"' AND `date` = '"+str(date)+"'"
        #sql = "SELECT * FROM `bargain_money_data` WHERE `operator` = '"+str(operator)+"' AND `date` = '2021-07-21'"
        
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    
    
    stock_name = myresult[0][2]
    if operator == "KGI_taipei":
        KGI_determine.KGI_taipei_module(type)
    elif operator == "lynch":
        pass



determine("KGI_taipei", time_combination, query_date, 'ticket')
determine("KGI_taipei", time_combination, query_date, 'money')
