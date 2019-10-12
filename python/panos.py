#!/usr/bin/env python

import pandevice
from pandevice import firewall
from getpass import getpass
import sys

hostname = input("Device hostname: ")
username = input("Device username: ")
# this should be getpass but it doesnt work on Windows
password = input("Device password: ")
# Non Windows alternative
#password = getpass("Device password: ")

def fw_connect(hostname,username,password):
    try:
        fw= pandevice.firewall.Firewall(hostname, username, password)
        info = fw.refresh_system_info()
        print(f'Firewall system info: {info}\n')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    fw_connect(hostname,username,password)
