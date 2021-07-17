import fetcher
import datetime
import mysql.connector

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

def combine(pr_data):
    new_data = ""
    pr_data = list(pr_data)
    try:
        pr_data.remove(",")
        new_data = int(new_data.join(pr_data))
    except:
        new_data = int(new_data.join(pr_data))

    return new_data

def insert_command(data, operator, type): #data="資料", operator="操作券商", type==>money="以金額計價" ticket="以張數計價"
    total_affect = 0
    for i in range(1, 21):
        stock_name = str(data[0])
        buy_amount = combine(data[1])
        sell_amount = combine(data[2])
        total_amount = combine(data[3])

        if type == "money":
            sql = "INSERT INTO `bargain_money_data`(`date`, `stock_name`, `buy_amount`, `sell_amount`, `total_amount`, `operator`, `daily_rank`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        elif type == "ticket":
            sql = "INSERT INTO `bargain_ticket_data`(`date`, `stock_name`, `buy_amount`, `sell_amount`, `total_amount`, `operator`, `daily_rank`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        val = time_combination, stock_name, buy_amount, sell_amount, total_amount, operator, i

        mycursor.execute(sql, val)
        mydb.commit()

        status = mycursor.rowcount
        total_affect += 1
        del data[0:4]

    return total_affect

