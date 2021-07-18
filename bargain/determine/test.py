import fetcher
import percentage_updater_new
import datetime
import sql_insert
import time

now = datetime.datetime.now()

time_combination = str(now.strftime("%Y"))+"-" + \
    str(now.strftime("%m"))+"-"+str(now.strftime("%d"))

#凱基(隔日沖)(隔日跌)(分點代號:9268)--------------------------------------------------------------------------------------------------------
#凱基-台北-金額
url_KGI_taipei_money = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=B&d=1;KGI_taipei"
#凱基-台北-張數
url_KGI_taipei_ticket = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=E&d=1;KGI_taipei" 

#元大(隔日沖)(隔日跌)(分點代號:9875)--------------------------------------------------------------------------------------------------------
#元大-土城永寧-金額
url_yuanta_tucheng_money = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9800&b=9875&c=B&d=1;yuanta_tucheng"
#元大-土城永寧-張數
url_yuanta_tucheng_ticket = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9800&b=9875&c=E&d=1;yuanta_tucheng"

#富邦(隔日沖)(隔日漲)(分點代號:9658)--------------------------------------------------------------------------------------------------------
#富邦-建國-金額
url_fubon_jiangguo_money = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9600&b=9658;fubon_jiangguo"
#富邦-建國-張數
url_fubon_jiangguo_ticket = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9600&b=9658&c=E&d=1;fubon_jiangguo"
#富邦-嘉義-金額(分點代號:9692)
url_fubon_chiayi_money = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9600&b=9692;fubon_chiayi"
#富邦-嘉義-張數
url_fubon_chiayi_ticket = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=9600&b=9692&c=E&d=1;fubon_chiayi"

#美林(連買2日)----------------------------------------------------------------------------------------------------------------
#美林-金額(分點代號:1440)
url_Lynch_money = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=1440&b=1440;lynch"
#美林-張數
url_Lynch_ticket = "http://jsjustweb.jihsun.com.tw/z/zg/zgb/zgb0.djhtm?a=1440&b=1440&c=E&d=1;lynch"

fetch_array_money = [url_KGI_taipei_money, url_yuanta_tucheng_money, url_fubon_jiangguo_money, url_fubon_chiayi_money, url_Lynch_money]
fetch_array_ticket = [url_KGI_taipei_ticket, url_yuanta_tucheng_ticket, url_fubon_jiangguo_ticket, url_fubon_chiayi_ticket, url_Lynch_ticket]

for item_money in fetch_array_money:
    time.sleep(1)
    data_seperator = item_money.split(';')
    data = fetcher.fetcher('linux', data_seperator[0])
    sql_insert.insert_command(data, data_seperator[1], 'money')

for item_ticket in fetch_array_ticket:
    time.sleep(1)
    data_seperator = item_ticket.split(';')
    data = fetcher.fetcher('linux', data_seperator[0])
    sql_insert.insert_command(data, data_seperator[1], 'ticket')
