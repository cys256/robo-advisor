
import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime
now = datetime.now()

def to_usd(myprice):
    return "${0:,.2f}".format(myprice)

load_dotenv() # go get env vars from the .env file

# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# make a request
#symbol = "MSFT" 
symbol = input("Please enter a valid stock ticker to see recommendation: ")
t = symbol.upper()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)
#print(type(response))
#print(response.status_code) #> 200
#print(response.text)

parsed_response = json.loads(response.text) # converts to dictionary

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) 
dates.sort(reverse = True)

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)

#breakpoint()


print("-------------------------")
print("SELECTED SYMBOL:", t)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
dt_string = now.strftime("%m/%d/%Y %H:%M %p")
print("REQUEST AT:", dt_string)
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")