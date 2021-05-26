import json
import requests
import datetime

def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys(".secret/keys.json")

url = 'https://api.foursquare.com/v2/users/83524656/checkins?oauth_token=' + keys["ACCESS_TOKEN"]

# Testing connection to get latest check-ins
params = dict(
    USER_ID='self',
    limit=5,
    sort='newestfirst',
    v=20200501
    )

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

#Printing the most recent 5 check-ins time created and location name
print([[datetime.datetime.utcfromtimestamp(a['createdAt']), a['venue']['name']] for a in data['response']['checkins']['items']])

