from ncclient import manager
import xmltodict
from pprint import  pprint
import logging

# logging.basicConfig(level=logging.DEBUG)

# router = {
#     "host": "ios-xe-mgmt.cisco.com",
#     "port": "10000",
#     "username": "developer",
#     "password": "C1sco12345"
# }

router = {
    "host": "192.168.1.211",
    "port": "830",
    "username": "admin",
    "password": "juniper1"
}

int_filter = """
  <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
      <GigabitEthernet>
        <name>1</name>
      </GigabitEthernet> 
      </interface> 
    </native>
        <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
      <interface>
      <name>GigabitEthernet1</name>
      </interface>
    </interfaces>
  </filter>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    netconf_response = m.get(int_filter)
    # print(netconf_response)

python_response = xmltodict.parse(netconf_response.xml)['rpc-reply']['data']
# pprint(python_response)

op = python_response["interfaces"]["interface"]
config = python_response["native"]['interface']['GigabitEthernet']

print(f"Name: GigabitEthernet{config['name']['#text']}")
print(f"Packets In: {op['statistics']['in-unicast-pkts']}")