#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

if os.getenv("NETMIKO_PASSWORD"):
    password = os.getenv("NETMIKO_PASSWORD")
else:
    getpass()

device = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "./ssh_config",
}

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show users")
    print(output)
