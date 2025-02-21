import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  6# Your latitude
MY_LONG = 6 # Your longitude

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude, iss_latitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5):
        print("close")
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_w = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_w.raise_for_status()
    data_w = response_w.json()
    sunrise = int(data_w["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_w["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

my_email = "email" #Email
password = "pass" #API password
while True:
    if is_iss_close() and is_dark():
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject: ISS PASSING\n\n LOOK UP...\n The ISS is close and it's visible")
    time.sleep(60)
