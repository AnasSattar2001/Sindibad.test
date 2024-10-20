import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# Check if the request was successful
if response.status_code == 200:
    for data in response.json()['items']:
        if data['answer_count'] == 0:
            print(data['title'])
            print(data['link'])
        else:
            print("skipped")
        print()  # Adds a blank line for better readability
else:
    print("Failed to retrieve data:", response.status_code)
