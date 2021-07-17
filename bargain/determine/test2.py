import re
a = '2303台積電'
regex00 = re.compile(r"\d+")

match = regex00.search(a)

print(match.group(0))

