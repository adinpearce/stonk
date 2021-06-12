from shioaji.data import Ticks
import shioaji as  sj
import pandas as pd

api = sj.Shioaji()

#login

account = api.login("S125235872", "adin2427")
'''
ticks = api.ticks(
    contract=api.Contracts.Stocks["2330"], 
    date="2021-06-11", 
    query_type=sj.constant.TicksQueryType.LastCount,
    last_cnt=1,
)
print(ticks)
'''
'''
kbars = api.kbars(api.Contracts.Stocks["2330"], start="2021-06-10", end="2021-06-11")
print(kbars)
'''
contracts = [api.Contracts.Stocks['2330']]
snapshots = api.snapshots(contracts)
print(snapshots)

high = snapshots[0]['high']
low = snapshots[0]['low']
open_price = snapshots[0]['open']
close_price = snapshots[0]['close']
avg_price = snapshots[0]['average_price']
total_volume = snapshots[0]['total_volume']

print(high)
print(low)
print(open_price)
print(close_price)
print(avg_price)
print(total_volume)