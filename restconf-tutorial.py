import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def printBytesAsJSON(bytes):
    print(json.dumps(json.loads(bytes), indent=2))
    
response = requests.get(
    url ="https://192.168.1.31/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
)

printBytesAsJSON(response.content)

response = requests.post(
    url = "https://192.168.1.31/restconf/data/Cisco-IOS-XE-native:native/interface",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json",
        'Content-Type': 'application/yang-data+json'
    },
    verify = False,
    data = json.dumps({
        "Cisco-IOS-XE-native:Loopback": {
            "name": 1,
            "ip": {
            "address": {
                "primary": {
                "address": "2.2.2.2",
                "mask": "255.255.255.255"
                }
            }
            }
        }
        }
    )
)
print(response.status_code)

response = requests.patch(
    url = "https://192.168.1.31/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=1",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json",
        'Content-Type': 'application/yang-data+json'
    },
    verify = False,
    data = json.dumps({
        "Cisco-IOS-XE-native:Loopback": {
            "ip": {
            "address": {
                "primary": {
                "address": "2.2.2.3",
                "mask": "255.255.255.255"
                }
            }
            }
        }
        }
    )
)

print(response.status_code)

response = requests.patch(
	url = 'https://192.168.1.31/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2',
	auth = ('admin', 'juniper1'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	data = json.dumps({
        "Cisco-IOS-XE-native:GigabitEthernet": {
            "name": "2",
            "ip": {
            "address": {
                "primary": {
                "address": "10.10.10.1",
                "mask": "255.255.255.0"
                }
            }
            },
            "mop": {
            "enabled": 'false',
            "sysid": 'false'
            },
        }
    }),
	verify = False)

# Print the HTTP response code
print('Response Code: ' + str(response.status_code))


response = requests.get(
    url ="https://192.168.1.31/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1/statistics/in-octets",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
).json()

print(json.dumps(response, indent=2))


# printBytesAsJSON(response.content)
# curl -H "Accept: application/yang-data+json" -k https://192.168.1.31/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/cpu-usage-processes/cpu-usage-process\=7,EDDRI_MAIN -u "admin:juniper1"
response = requests.get(
    url ="https://192.168.1.31/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/cpu-usage-processes/cpu-usage-process=7,EDDRI_MAIN/avg-run-time",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
).json()

print(json.dumps(response, indent=2))

response = requests.get(
    url ="https://192.168.1.31/restconf/data/Cisco-IOS-XE-native:native/hostname",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
).json()

print(json.dumps(response, indent=2))

# response = requests.get(
#     url ="http://192.168.1.46:8080/rpc/get-vrrp-information",
#     auth = ("admin", "juniper1"),
#     headers = {
#         "Accept": "application/yang-data+json"
#     },
#     verify = False
# )

# print(response.text)

response = requests.get(
    url ="https://192.168.1.31/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1",
    auth = ("admin", "juniper1"),
    headers = {
        "Accept": "application/yang-data+json"
    },
    verify = False
).json()


print(json.dumps(response, indent=2))
print(response["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
if response["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
    print("Interface is UP")