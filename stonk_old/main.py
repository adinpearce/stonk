import yahoo_finance_test as api
import datetime

'''
當日股價:
起始日:今日日期
截止日:明日日期

api:
time_counter(a, b)
    ==>a放"1970-01-01"
    ==>b放指定日期
        ==>格式(%Y-%m-%d)
'''


def catcher(stonk_num):
    now = datetime.datetime.now()

    today_date = str(now.strftime("%Y"))+"-" + \
        str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

    tomorrow = datetime.datetime.strptime(today_date, "%Y-%m-%d")
    tomorrow_transfer = tomorrow + datetime.timedelta(days=1)

    tomorrow_transfer_2 = str(tomorrow_transfer.strftime(
        "%Y")) + "-"+str(tomorrow_transfer.strftime("%m"))+"-"+str(tomorrow_transfer.strftime("%d"))

    # 時間計算
    '''
    start_date = api.time_counter("1970-01-01", today_date)
    end_date = api.time_counter("1970-01-01", tomorrow_transfer_2)
    '''
    start_date = api.time_counter("1970-01-01", str(today_date))
    end_date = api.time_counter("1970-01-01", str(tomorrow_transfer_2))
    # 股價抓取
    data = api.json_extraction(api.retriver(
        stonk_num, start_date, end_date, 0))
    # 上傳資料庫
    status = api.db_in(today_date, data, str(stonk_num))
    return status


#print(catcher(2302))
