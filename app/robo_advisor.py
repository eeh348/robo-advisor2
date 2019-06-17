# app/robo_advisor.py

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
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")