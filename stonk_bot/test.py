import re

re_date = re.compile(r"(\d+)-(\d+)-(\d+)")
re_date_t2 = re.compile(r"(\d+)/(\d+)/(\d+)")

a= "台中"

match1 = re_date.search(a)
match = re_date_t2.search(a)

if match != None or match1 != None:
    print("confirm")
else:
    print("false")