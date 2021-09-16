#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "file_system": "flash:",
}
arista = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "file_system": "/mnt/flash",
}
junos = {
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "file_system": "/var/tmp",
}
nxos = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "file_system": "bootflash:",
}

source_file = "test1.txt"
dest_file = "testa.txt"
direction = "put"

for net_device in (cisco, arista, junos, nxos):
    file_system = net_device.pop("file_system")

    # Create the Netmiko SSH connection
    ssh_conn = ConnectHandler(**net_device)
    transfer_dict = file_transfer(
        ssh_conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system=file_system,
        direction=direction,
        overwrite_file=True,
    )
    print(transfer_dict)
    pause = input("Hit enter to continue: ")
