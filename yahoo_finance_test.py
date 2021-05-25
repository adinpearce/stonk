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

    diff_time = str(c_time).strip(" days, 0:00:00")

    diff_time = int(diff_time)

    diff_time = diff_time - 8
    seconds = diff_time * 24 * 60 * 60

    return seconds


def retriver(stock_num, period1, period2, state):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/"+str(stock_num)+".TW?period1="+str(
        period1)+"&period2="+str(period2)+"&interval=1d&events=history&=hP2rOschxO0"

    response = requests.get(url)
    return_data = json.dumps(response.text)
    return return_data


def json_extraction(json_data):
    #data = json.loads(json_data)
    json_data = dict(json_data)
    got_data = json_data["low"]
    return got_data


period1 = time_counter(a, "2021-05-20")
period2 = time_counter(a, time_combination)

#print(retriver(2330, period1, period2, 0))
print(json_extraction(retriver(2330, period1, period2, 0)))
