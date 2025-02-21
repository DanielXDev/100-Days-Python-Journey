import requests

LAT= 7.3775355
LONG = 3.9470396

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

print(data['results'])