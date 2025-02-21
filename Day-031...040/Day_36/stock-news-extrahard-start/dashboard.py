import streamlit as st
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
NEW_API_KEY = os.getenv("NEW_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

# Define default stocks
STOCKS = ["TSLA", "AAPL", "AMZN"]

# Streamlit UI
st.title("📈 Stock & News Dashboard")
selected_stock = st.selectbox("Choose a stock:", STOCKS)

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
formatted_date = yesterday.strftime("%Y-%m-%d")


# Fetch stock data
def get_stock_data(stock_symbol):
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "outputsize": "compact",
        "apikey": STOCK_API_KEY
    }
    stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
    stock_data = stock_response.json()

    if "Time Series (Daily)" not in stock_data:
        return None, None, None

    dates = sorted(stock_data["Time Series (Daily)"].keys(), reverse=True)
    latest_date, second_latest_date = dates[:2]
    latest_close = float(stock_data["Time Series (Daily)"][latest_date]["4. close"])
    second_latest_close = float(stock_data["Time Series (Daily)"][second_latest_date]["4. close"])
    price_change = round(((latest_close - second_latest_close) / second_latest_close) * 100, 2)

    return latest_close, second_latest_close, price_change


# Fetch news data
def get_stock_news(company_name):
    news_params = {
        "q": company_name,
        "from": formatted_date,
        "sortBy": "popularity",
        "apiKey": NEW_API_KEY
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()

    return news_data["articles"][:3] if "articles" in news_data else []


# Display stock data
latest_close, second_latest_close, price_change = get_stock_data(selected_stock)
if latest_close:
    st.subheader(f"💰 {selected_stock} Stock Performance")
    st.write(f"Latest Close: **${latest_close}**")
    st.write(f"Previous Close: **${second_latest_close}**")

    if price_change < 0:
        st.error(f"🔻 Price Change: {price_change}%")
    else:
        st.success(f"📈🆙 Price Change: {price_change}%")
else:
    st.warning("Stock data unavailable. Try again later.")

# Display news
st.subheader(f"📰 Latest News on {selected_stock}")
news_articles = get_stock_news(selected_stock)
if news_articles:
    for news in news_articles:
        st.write(f"**{news['title']}**")
        st.write(news['description'])
        st.write(f"[Read More]({news['url']})")
else:
    st.warning("No news articles found.")

