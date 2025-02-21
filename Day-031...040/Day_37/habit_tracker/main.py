from datetime import datetime

import requests


TOKEN = "TOKEN"
USERNAME = "USERNAME"
GRAPH_NAME = "Coding Graph"
GRAPH_ID = "graph2"

pixel_endpoint = "https://pixe.la/v1/users"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "hours",
    "type": "int",
    "color": "momiji"
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}
graph_pixel_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18"
}
response = requests.put(url=graph_pixel_endpoint, json=pixel_config, headers=graph_headers)
print(response.text)



