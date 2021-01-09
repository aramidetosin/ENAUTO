import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

response = requests.get(
    url ="https://api.discogs.com/releases/249504",
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
).json()

print(json.dumps(response, indent=2))
for i in range(0, 30):
    response = requests.get(
        url ="https://api.discogs.com/releases/249504",
        headers = {
            "Accept": "application/yang-data+json"
        },
        verify = False
    )

    print(response)