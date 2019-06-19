# app/robo_advisor.py

import requests
import json
import csv
import os

#define functions
def to_usd(price):
    price_usd = "${:,.2f}".format(price)
    return price_usd

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)

#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) #type 200
#print(response.text) #string

parsed_response = json.loads(response.text)

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

#while True:
#    #ask user for stock symbol
#    user_input = input("Please input a product company stock symbol:")
#    
#    if user_input.isalpha() and len(user_input) < 6:
#        user_input = user_input.upper()
#        break
#    else:
#        print("Input must be A-Z characters only and less than or equal to 5 characters")

user_input = "AMAZ"


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") #try to add multiple inputs later

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp","open","high", "low", "close","volume"])
    writer.writeheader() # uses fieldnames set above
    #breakpoint()
    for d in dates:
        daily_prices = tsd[d]
        writer.writerow({
            "timestamp": d,
            "open": daily_prices["1. open"]),
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })



print(user_input)

print("-------------------------")
print("SELECTED SYMBOL: " + user_input)
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
