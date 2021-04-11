from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests

total_array = []

def cleaner(result):
    soup = BeautifulSoup(result.text, 'html.parser')

    stock_full = soup.find('table', attrs={'class', 't01'})
    full_array = []
    clean_array_full = []

    stock_1 = stock_full.find_all('tr')
    del stock_1[0:2]

    for data in stock_1:
        data1 = data.find_all('td')
        del data1[0]
        partial_array = []
        for all in data1:
            partial_array.append(all.text)
        full_array.append(partial_array)

    for data in full_array:
        clean_array = []
        for partial in data:
            out = "".join(partial.split())
            clean_array.append(out)
        clean_array_full.append(clean_array)


    return clean_array_full

for i in range(1, 20):
    if (i == 1 or i ==5 or i == 10):
        result = requests.get("http://jsjustweb.jihsun.com.tw/z/zg/zg_F_0_"+str(i)+".djhtm")
        total_array.append(cleaner(result))

for data in total_array:
    for layer2 in data:
        print(layer2)
    print("="*50)
        