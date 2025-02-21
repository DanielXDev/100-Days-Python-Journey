from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

NUTRI_API = os.getenv("NUTRI_API")
NUTRI_ID = os.getenv("NUTRI_ID")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_API
}

# Get the user's input about their workout
params = {
    "query": input("What exersice do you do today?  ")
}

#Get the data about the exercise and th calories burnt
nutri_response = requests.post(url=endpoint, json=params, headers=headers)
data = nutri_response.json()
print(data)
today = datetime.now()

#Save the data and save it on the spreadsheet
for ex in data["exercises"]:
    sheety_endpoint = "https://api.sheety.co/d0ae71ec97ca499f81daef837a5c98b4/myWorkouts/workouts"
    sheety_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": f"{today.time()}",
            "exercise": ex["name"],
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }
    sheety_headers = {
        "Authorization": os.getenv("SHEETY_AUTH")
    }

    response = requests.post(url=sheety_endpoint, json=sheety_config, headers=sheety_headers)
    print(response.json())