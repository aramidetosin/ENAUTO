from ncclient import manager
from router_info import router

conig_template = open("./ios_config.xml").read()

netconf_config = conig_template.format(
    interface_name='2',
    interface_desc='Tosin wuz here',
    interface_ip='10.1.1.1',
    interface_mask='255.255.255.0',
    enable='true'
)

print(netconf_config)

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="running")

print(response)
