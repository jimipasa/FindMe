import os
from googlefinance import getQuotes
import json
tickers = {'AAPL':'Apple ','NFLX':'Netflix ', 'V' :'Visa ', 'LUV':'SouthWest '}
for tick in tickers.keys():
    result = json.dumps(getQuotes(tick), indent=2)
    LTPrice = json.loads(json.dumps(getQuotes(tick), indent=2))[0]['LastTradePrice']
    LTTime = json.loads(json.dumps(getQuotes(tick), indent=2))[0]['LastTradeDateTimeLong']
    print ('Last traded price for ' + tickers[tick] + 'on '+ LTTime +' is ' + LTPrice + ' dollars')
    announce = 'say Last traded price for ' + tickers[tick] + 'on '+ LTTime +' is ' + LTPrice + ' dollars'
    os.system(announce)