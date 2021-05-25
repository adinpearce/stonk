import datetime
import requests
import json
import jsonpath

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

    print(url)
    print("="*50)

    response = requests.get(url)
    return_data = json.dumps(response.text)
    return response.text


def json_extraction(json_data):
    data = json.loads(json_data)

    open = data['chart']['result'][0]['indicators']['quote'][0]['open']
    close = data['chart']['result'][0]['indicators']['quote'][0]['close']
    low = data['chart']['result'][0]['indicators']['quote'][0]['low']
    high = data['chart']['result'][0]['indicators']['quote'][0]['high']
    volume = data['chart']['result'][0]['indicators']['quote'][0]['volume']
    return open, close, low, high, volume


period1 = time_counter(a, "2021-05-25")
period2 = time_counter(a, "2021-05-26")

print(period1, period2)

#print(retriver(2330, period1, period2, 0))
print(json_extraction(retriver(2330, period1, period2, 0)))
