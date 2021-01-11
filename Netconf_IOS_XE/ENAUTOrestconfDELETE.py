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

url =f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=Loopback100"

response = requests.get(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False,
).json()

print(json.dumps(response, indent=2))

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"
url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100"


response = requests.delete(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False,
)

if response.status_code == 204:
    print(response)
    print(response.text)