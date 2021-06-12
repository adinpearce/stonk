import shioaji as sj
import pandas as pd
import time


api = sj.Shioaji()

#login

account = api.login("S125235872", "adin2427")
'''
api.activate_ca(
    ca_path="C:/ekey/551/S125235872/S/Sinopac.pfx",
    ca_passwd="S125235872",
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)

api.login(
    person_id="S125235872", 
    passwd="adin2427", 
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)
'''
contract_2890 = api.Contracts.Stocks["2890"]
#print(contract_2890)

api.quote.subscribe(api.Contracts.Stocks["2330"], quote_type='tick')
time.sleep(5)