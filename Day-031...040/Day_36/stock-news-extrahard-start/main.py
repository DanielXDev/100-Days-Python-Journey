import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


STOCK = input("Enter the stock symbol (e.g., TSLA, AAPL, AMZN): ").upper()
COMPANY_NAME = input("Enter the company name: ").title()
NEW_API_KEY = os.getenv("NEW_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
yesterday = datetime.now() - timedelta(days=1)
formatted_date = yesterday.strftime("%Y-%m-%d")

# Check yesterday's closing price for the stock and for the day before.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data["Time Series (Daily)"])
dates = sorted(stock_data["Time Series (Daily)"].keys(), reverse=True)  # Sort dates in descending order (latest first)
latest_date, second_latest_date = dates[:2]
latest_close = float(stock_data["Time Series (Daily)"][latest_date]["4. close"])
second_latest_close = float(stock_data["Time Series (Daily)"][second_latest_date]["4. close"])
price_difference = round(((latest_close - second_latest_close)/second_latest_close) * 100, 2)
print(price_difference)
if price_difference < 0:
    replace_sym = str(price_difference).replace("-", "🔻")
    print(replace_sym)
else:
    replace_sym = f"📈🆙{price_difference}"
    print(replace_sym)

# Get the latest new about the stock and send an SMS.
news_params = {
    "q": COMPANY_NAME,
    "from": f"{formatted_date}",
    "sortBy": "popularity",
    "apiKey":NEW_API_KEY
}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
latest_three_news = news_data["articles"][:3]
for news in latest_three_news:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{COMPANY_NAME}: {replace_sym}%\nHeadline: {news["title"]}\nBrief: {news["description"]}",
        from_="SENDER",
        to="RECEIVER",
    )


