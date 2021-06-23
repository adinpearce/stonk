import datetime


#datetime_initialize
now = datetime.datetime.now()
today_date = str(now.strftime("%Y"))+"-" + str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

today_date_datetime = datetime.datetime.strptime(today_date, "%Y-%m-%d")


est_date = "2021-06-10"
est_date_datetime = datetime.datetime.strptime(est_date, "%Y-%m-%d")

conflict_time = today_date_datetime - est_date_datetime
print ((str(conflict_time).split(" days, 0:00:00"))[0])