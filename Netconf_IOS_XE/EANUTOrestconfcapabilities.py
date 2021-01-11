import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

router = {
    "host": "192.168.1.211",
    "port": "443",
    "user": "admin",
    "password": "juniper1"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

response = requests.get(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False
)

# print(json.dumps(response, indent=2))
if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)