import requests

# Variables for Strava API authentication
clientid = "288575"
client_secret = "927ae7bc6d8db5972ea61513213c9eebedcb8da6"
access_token = "d7eaee83df8867fcfc9b129f9d58073c9318a4a3"
refresh_token = "a16d11c9984e68cdf469b2a1fa9f3fedc516302f"

# Goal URL for Strava API
goal_url = "https://www.strava.com/oauth/token"

# Dictionary to hold the data for the POST request
data = {
    "client_id": clientid,
    "client_secret": client_secret,
    "code": "e5a152bcc9932ffc12e9b62ce5c480199a4881b9",
    "grant_type": "authorization_code"
}

# response
response = requests.post(goal_url, data=data)

# Check what Strava API returns
print(response.json())

my_token = response.json()["access_token"]
goal_url2 = "https://www.strava.com/api/v3/athlete/activities"
headers = {"Authorization": "Bearer " + my_token}
activities_response = requests.get(goal_url2, headers=headers)
print(activities_response.json())

import json

# Speichert alle heruntergeladenen Aktivitäten in einer lokalen Datei
with open("myactivities.json", "w", encoding="utf-8") as f:
    json.dump(activities_response.json(), f, indent=2)

print("Daten wurden erfolgreich in 'myactivities.json' gespeichert!")
