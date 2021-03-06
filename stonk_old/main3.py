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
    # 時間計算
    start_date = api.time_counter("1970-01-01", str(today))
    end_date = api.time_counter("1970-01-01", str(tomorrow_c))
    # 股價抓取
    data = api.json_extraction(api.retriver(
        stonk_num, start_date, end_date, 0))
    # 上傳資料庫
    status = api.db_in(str(today), data, str(stonk_num))
    return status


time_list1 = ["2021-07-12", "2021-07-13", "2021-07-14"]
time_list2 = ["2021-07-13", "2021-07-14", "2021-07-15"]


stonk_list = [2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6434, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]
#stonk_list = [2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]
#print(catcher(2302, "2021-05-28", "2021-05-29"))
counter = 0
for num in stonk_list:
    counter += 1
 
    for i in range(1, len(time_list1)):
        print(time_list1[i], time_list2[i])
        print(catcher(num, time_list1[i], time_list2[i]))
        time.sleep(1)

    print(("=")*50+str(num))
    time.sleep(10)

