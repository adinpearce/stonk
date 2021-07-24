
import datetime
now = datetime.datetime.now()
current_time = str(now.strftime("%H"))+":"+str(now.strftime("%M"))

print(current_time)
