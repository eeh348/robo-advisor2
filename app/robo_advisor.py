# app/robo_advisor.py

import requests
import json 

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)

#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) #type 200
#print(response.text) #string

parsed_response = json.loads(response.text)

tsd = parsed_response['Time Series (Daily)']

dates = list(tsd.keys())  #may need to update to sort for latest date

latest_date = dates[0]

#capture variables
last_refresh = parsed_response["Meta Data"]['3. Last Refreshed']
last_close = tsd[last_refresh]['4. close']
recent_high = tsd[last_refresh]['2. high']
recent_low = tsd[last_refresh]['3. low']

breakpoint()

def get_stock_price(stock):
    pass

while True:
    #ask user for stock symbol
    user_input = input("Please input a product company stock symbol:")
    
    if user_input.isalpha() and len(user_input) < 6:
        user_input = user_input.upper()
        break
    else:
        print("Input must be A-Z characters only and less than or equal to 5 characters")

print(user_input)

print("-------------------------")
print("SELECTED SYMBOL: " + user_input)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refresh}")
print(f"LATEST CLOSE: {last_close}") #format $
print(f"RECENT HIGH: {recent_high}") #format $
print(f"RECENT LOW: {recent_low}") #format $
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")