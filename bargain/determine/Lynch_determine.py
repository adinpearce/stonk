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

sql = "SELECT * FROM `stock_day` ORDER BY `date` DESC LIMIT 5"
mycursor.execute(sql)

date = mycursor.fetchall()

#query_date = "`date` = '"+time_combination+"' OR `date` = '"+date[0][1]+"' OR `date` = '"+date[0][2]+"' OR `date` = '"+date[0][3]+"' OR `date` = '"+date[0][4]+"'"
Date_M1 = date[1][0]
Date_M2 = date[2][0]

try:
    Date_M3 = date[3][0]
except :
    Date_M3 = ""

try:
    Date_M4 = date[4][0]
except :
    Date_M4 = ""


def fetcher(date, type):
    if type == "money":
        sql = "SELECT * FROM `bargain_money_data` WHERE `date` = '"+date+"' AND `operator` = 'lynch'"
    elif type == "ticket":
        sql = "SELECT * FROM `bargain_ticket_data` WHERE `date` = '"+date+"' AND `operator` = 'lynch'"

    mycursor.execute(sql)

    fetch = mycursor.fetchall()
    first_track = []

    for item in fetch:
        stock_name = item[2]
        first_track.append(stock_name)

    return first_track

def lynch_determine_module(type):
    currentD = fetcher(time_combination, type)
    currentDM1  = fetcher(Date_M1, type)
    currentDM2  = fetcher(Date_M2, type)
    currentDM3  = fetcher(Date_M3, type)
    #currentDM4  = fetcher(Date_M4, type)

    for item in currentD:
        buy_count = [1,0,0,0,0]
        if item in currentDM1:
            buy_count[1] == 1
        
        if item in currentDM2:
            buy_count[2] == 1
        
        if item in currentDM3:
            buy_count[3] == 1
        '''
        if item in currentDM4:
            buy_count[4] == 1
        '''
        buy_date = buy_count.index(0)

        print(str(item) + "連買==>" + str(buy_date))

lynch_determine_module('money')



