from ncclient import manager
import logging
import xmltodict
# logging.basicConfig(level=logging.DEBUG)


router = {
    "host": "192.168.1.211",
    "port": "830",
    "username": "admin",
    "password": "juniper1"
}



with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
# with manager.connect(**router, hostkey_verify=False) as m:
#     print("hello World")
    for capability in m.server_capabilities:
        print("*"*25)
        print(" ")
        print(capability)