import yahoo_finance_test as api
import datetime
import time

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


def catcher(stonk_num, today, tomorrow_c):
    now = datetime.datetime.now()

    today_date = str(now.strftime("%Y"))+"-" + \
        str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

    tomorrow = datetime.datetime.strptime(today_date, "%Y-%m-%d")
    tomorrow_transfer = tomorrow + datetime.timedelta(days=1)

    tomorrow_transfer_2 = str(tomorrow_transfer.strftime(
        "%Y")) + "-"+str(tomorrow_transfer.strftime("%m"))+"-"+str(tomorrow_transfer.strftime("%d"))

    # 時間計算
    start_date = api.time_counter("1970-01-01", str(today))
    end_date = api.time_counter("1970-01-01", str(tomorrow_c))
    # 股價抓取
    data = api.json_extraction(api.retriver(
        stonk_num, start_date, end_date, 0))
    # 上傳資料庫
    status = api.db_in(str(today), data, str(stonk_num))
    return status

stonk_list = [2302, 2303, 2329, 2330, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]


#stonk_list = [6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]

for data in stonk_list:
    print(catcher(data, "2021-06-11", "2021-06-12"))
    time.sleep(2)
