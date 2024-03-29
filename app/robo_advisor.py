# app/robo_advisor.py

import requests
import datetime
import json
import csv
import os
import statistics
from dotenv import load_dotenv

#find time
now = datetime.datetime.now()

#define functions
def to_usd(price):
    price_usd = "${:,.2f}".format(price)
    return price_usd

#capture keys
load_dotenv()
my_cred = os.environ.get("ALPHAVANTAGE_API_KEY")

#Create list for multiple user inputs
symbol_list = []

#capture multiple inputs in a list until user types DONE; does not validate if it's a valid stock symbol
while True:
    #ask user for stock symbol
    symbol = input("Please input a product company stock symbol:")
    symbol = symbol.upper()

    if symbol == "DONE":
        break
    elif symbol.isalpha() and len(symbol) < 6:
        #symbol = symbol.upper()
        symbol_list.append(symbol.upper())
    else:
        print("Input must be A-Z characters only and less than or equal to 5 characters")

    #breakpoint()

x = 0

#iterate through symbols
for s in symbol_list:
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={s}&apikey={my_cred}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)

    x = x + 1

    #check to see if request url returns an error message
    valid_symbol = str(parsed_response.keys())

    if valid_symbol == "dict_keys(['Error Message'])":
        if x == len(symbol_list):
            print(f"{s} is not a valid stock symbol. Exiting...")
            exit()
        else:
            print(f"{s} is not a valid stock symbol. Continuing...")
        continue
    else:
        pass

    #breakpoint()

    tsd = parsed_response['Time Series (Daily)']

    dates = list(tsd.keys())  #may need to update to sort for latest date

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

    #write to file
    filename = f"{s}.csv"
    csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", filename) #try to add multiple inputs later
    
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

    #recommendation engine
    if float(last_close) < statistics.median(highs):
        rec = "BUY!"
        reason = "THE CLOSING PRICE IS LOWER THAN THE MEDIAN PRICE FOR THE LAST 100 DAYS."
    else:
        rec = "DO NOT BUY!"
        reason = "THE CLOSING PRICE IS HIGHER THAN THE MEDIAN PRICE FOR THE LAST 100 DAYS."

    print("-------------------------")
    print(f"SELECTED SYMBOL: {s}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("RUN AT: " + str(now.strftime("%B %d, %Y %H:%M %p")))
    print("-------------------------")
    print(f"LATEST DAY: {last_refresh}")
    print(f"LATEST CLOSE: {to_usd(float(last_close))} ")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print(f"100-DAY MEDIAN: {to_usd(statistics.median(highs))}")
    print("-------------------------")
    print(f"RECOMMENDATION: {rec}") 
    print(f"RECOMMENDATION REASON: {reason}")
    print("-------------------------")
    print(f"WRITING DATA TO CSV... {csv_file_path} ")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")
