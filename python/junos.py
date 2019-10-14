#!/usr/bin/env python
# test 
from jnpr.junos import Device
from getpass import getpass
import sys

hostname = input("Device hostname: ")
username = input("Device username: ")
# this should be getpass but it doesnt work on Windows
password = input("Device password: ")
# Non Windows alternative
#password = getpass("Device password: ")

dev = Device(host=hostname, user=username, passwd=password)
try:
    dev.open()
except Exception as err:
    print (err)
    sys.exit(1)

print (dev.facts)
dev.close()
print('done')
