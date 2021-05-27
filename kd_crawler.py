import datetime
from os import close
import requests
import json
import jsonpath
import mysql.connector

url = "https://www.wantgoo.com/stock/2330/technical-chart"

response = requests.get(url)
print(response)
