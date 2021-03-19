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

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/"

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Added by CBT Nuggets",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.100.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

# url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface"

# payload = {
#   "Cisco-IOS-XE-native:Loopback": {
#     "name": 100,
#     "description": "Added by CBT Nuggets",
#     "ip": {
#       "address": {
#         "primary": {
#           "address": "172.16.100.1",
#           "mask": "255.255.255.0"
#         }
#       }
#     }
#   }
# }

response = requests.post(
    url=url,
    headers=headers,
    auth=(
        router['user'],
        router['password']
    ),
    verify=False,
    data=json.dumps(payload)
)

if response.status_code == 201:
    print(response)
    print(response.text)
    
# curl -H "Accept: application/yang-data+json" -k https://192.168.1.211/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100 -u "admin:juniper1"

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