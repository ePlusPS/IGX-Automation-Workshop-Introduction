#!/usr/bin/env python

from pandriver import *
from getpass import getpass
import sys

hostname = input("Device hostname: ")
username = input("Device username: ")
password = getpass("Device password: ")

try:
    fw = pandevice.firewall.Firewall(hostname, username, password)
    print(f'Firewall system info: {pano.refresh_system_info()}\n')
except:
    print('Failed to connect to Firewall')
