
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

while True:
    symbol = input("PLEASE ENTER A VALID STOCK TICKER TO SEE RECOMMENDATION: ")
    t = symbol.upper()
    if len(symbol) < 5:
        print("GOOD CHOICE!")
        break
    else:
        print("PLEASE ENTER VALID STOCK TICKER")
        continue


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
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)



#breakpoint()

try:
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
    print(f"RECENT LOW: {to_usd(float(recent_low))}")

    print("-------------------------")
    if float(latest_close) < 1.2 * float(recent_low):
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: BECAUSE", t, "STOCK'S LATEST CLOSING PRICE IS LESS THAN 20% ABOVE ITS RECENT LOW")
    else:
        print("RECOMMENDATION: DON'T BUY!")
        print("RECOMMENDATION REASON: BECAUSE", t, "STOCK'S LATEST CLOSING PRICE IS GREATER THAN 20% ABOVE ITS RECENT LOW")

    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")
except KeyError:
    print("OOPS")


#from pandas import read_csv

#csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

#historical_prices = read_csv(response.text)

#with open(csv_file_path, "w") as csv_file:
    #print(historical_prices.head())