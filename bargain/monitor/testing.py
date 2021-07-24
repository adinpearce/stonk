import requests
from bs4 import BeautifulSoup

a = requests.get("https://forum.gamer.com.tw/B.php?bsn=37689%22")

soup = BeautifulSoup(a.text,"html.parser")

sel = soup.find_all(class_ = "b-list__main__title")

for g in sel:
    print(g.text)