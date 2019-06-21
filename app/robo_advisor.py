# app/robo_advisor.py

import requests
import json
import csv
import os
from dotenv import load_dotenv

#define functions
def to_usd(price):
    price_usd = "${:,.2f}".format(price)
    return price_usd

#capture keys
load_dotenv()
my_cred = os.environ.get("ALPHAVANTAGE_API_KEY")

while True:
    #ask user for stock symbol
    symbol = input("Please input a product company stock symbol:")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={my_cred}"
    response = requests.get(request_url)

    if symbol.isalpha() and len(symbol) < 6 and response.status_code == 200:
        symbol = symbol.upper()
        break
    else:
        print("Input must be A-Z characters only and less than or equal to 5 characters")

#user_input = "MSFT"

#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) #type 200
#print(response.text) #string

parsed_response = json.loads(response.text)

#breakpoint()

#valid code
if parsed_response.keys() == ['Error Message']:
    print(f"{symbol} is not a valid stock symbol. Exiting...")
    exit()
else:
    pass
    

tsd = parsed_response['Time Series (Daily)']

dates = list(tsd.keys())  #may need to update to sort for latest date

#high = list(tsd['2. high'])

latest_date = dates[0]

#capture variables
last_refresh = parsed_response["Meta Data"]['3. Last Refreshed']

highs = []
lows = []

#compile list of high prices / update to compile the values as a list
for d in dates:
    high_price = tsd[d]['2. high']
    highs.append(float(high_price))
    low_price = tsd[d]['3. low']
    lows.append(float(low_price))
    pass

last_close = tsd[latest_date]['4. close']

recent_high = max(highs)
recent_low = min(lows)

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") #try to add multiple inputs later

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp","open","high", "low", "close","volume"])
    writer.writeheader() # uses fieldnames set above
    #breakpoint()
    for d in dates:
        daily_prices = tsd[d]
        writer.writerow({
            "timestamp": d,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })

#print(symbol)

print("-------------------------")
print("SELECTED SYMBOL: " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refresh}")
print(f"LATEST CLOSE: {to_usd(float(last_close))} ")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!") 
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV... {csv_file_path} ")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
