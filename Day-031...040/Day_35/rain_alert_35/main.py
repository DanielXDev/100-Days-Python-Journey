import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
print(len(data["list"]))
bring_umb = False
for hour in data["list"]:
    if hour["weather"][0]["id"] < 700:
        bring_umb = True

if bring_umb:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's gonna rain today, bring an umbrella☔",
        from_="SENDER",
        to="RECEIVER",
    )
else:
    print("A good clear day, I don't think it'll rain today")