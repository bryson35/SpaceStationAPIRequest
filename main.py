import requests
import json

# Function that prints the data from the API in JSON format
def jprint(obj):
    #create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Use Open Notify API to get current people in space
response = requests.get("http://api.open-notify.org/astros.json")

#display all people currently in soace along with their spacecrafts
print("Current people in space right now, along with their spacecrafts")
jprint(response.json())

#Extract all names of people currently in space
people = response.json()["people"]

names = []

for name in people:
    n = name["name"]
    names.append(n)

print(f'All names are: {names}')







