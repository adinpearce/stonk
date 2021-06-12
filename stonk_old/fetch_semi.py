import requests
'''
CREATE TABLE `stonk`.`2337` ( `date` VARCHAR(255) NOT NULL , `open` TEXT NOT NULL , `close` TEXT NOT NULL , `high` TEXT NOT NULL , `low` TEXT NOT NULL , `volume` TEXT NOT NULL , `k` TEXT NOT NULL , `d` TEXT NOT NULL , PRIMARY KEY (`date`)) ENGINE = InnoDB;
'''


url = "https://pchome.megatime.com.tw/group/mkt0/cid24.html"
response = requests.get(url)
print(response.text)
