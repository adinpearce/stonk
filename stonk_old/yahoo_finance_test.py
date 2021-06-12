import datetime
from os import close
import requests
import json
import mysql.connector

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))
a = "1970-01-01"


def time_counter(a, b):
    a_time = datetime.datetime.strptime(a, "%Y-%m-%d")
    b_time = datetime.datetime.strptime(b, "%Y-%m-%d")

    c_time = b_time - a_time

    diff_time = c_time.days

    diff_time = int(diff_time)

    seconds = diff_time * 24 * 60 * 60 - 28800

    return seconds


def retriver(stock_num, period1, period2, state):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/"+str(stock_num)+".TW?period1="+str(
        period1)+"&period2="+str(period2)+"&interval=1d&events=history&=hP2rOschxO0"

    response = requests.get(url)
    return_data = json.dumps(response.text)
    return response.text


def data_cleaner(data):
    data = str(data).strip("[")
    data = data.strip("]")

    return data


def json_extraction(json_data):
    data = json.loads(json_data)

    open = data_cleaner(
        str(data['chart']['result'][0]['indicators']['quote'][0]['open']))
    close = data_cleaner(
        str(data['chart']['result'][0]['indicators']['quote'][0]['close']))
    low = data_cleaner(
        str(data['chart']['result'][0]['indicators']['quote'][0]['low']))
    high = data_cleaner(
        str(data['chart']['result'][0]['indicators']['quote'][0]['high']))
    volume = data_cleaner(str(data['chart']['result'][0]
                              ['indicators']['quote'][0]['volume']))

    open = round(float(open), 2)
    close = round(float(close), 2)
    low = round(float(low), 2)
    high = round(float(high), 2)
    volume = round(float(volume), 2)

    return open, close, low, high, volume


def db_in(date, data, stonk_num):
    mydb = mysql.connector.connect(
        host="220.135.176.190",
        user="k20",
        password="jona789521456",
        database="stonk",
        auth_plugin="mysql_native_password"
    )

    mycursor = mydb.cursor()

    open = data_cleaner(str(data[0]))
    close = data_cleaner(str(data[1]))
    low = data_cleaner(str(data[2]))
    high = data_cleaner(str(data[3]))
    volume = data_cleaner(str(data[4]))

    try:
        sql = "INSERT INTO `" + \
            str(stonk_num) + \
            "`(`date`, `open`, `close`, `high`, `low`, `volume`, `k`, `d`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = date, open, close, high, low, volume, "", ""
        mycursor.execute(sql, val)
        mydb.commit()
        return "success"
    except Exception as db_in_error:
        return db_in_error


'''
period1 = time_counter(a, "2021-05-10")
period2 = time_counter(a, "2021-05-15")

print(period1, period2)

#print(retriver(2330, period1, period2, 0))
data = json_extraction(retriver(2330, period1, period2, 0))
for element in data:
    print(element)
#print(db_in(time_combination, data, "2330"))
'''
