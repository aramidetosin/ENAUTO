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

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

response = requests.get(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False
).json()

print(json.dumps(response, indent=2))

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
# url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False
).json()

print(json.dumps(response, indent=2))
# print(response["Cisco-IOS-XE-interfaces-oper:interface"]['statistics']['in-unicast-pkts'])