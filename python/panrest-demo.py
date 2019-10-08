#!/usr/bin/env python
# import the modules we need for this script
import requests
requests.packages.urllib3.disable_warnings()
import xml.etree.ElementTree as xt
import json
import sys
import os
import getpass
import time

# set global variables
# you can leave these blank because we will check for them
hostname = '3.220.149.237'
username = 'apiuser'
password = 'apiuser'
apikey = ''


# check we have the hostname and credentials
def get_creds():

    # set the variables to global so we adjust the globals
    global hostname
    global username
    global password

    # gather the hostname and credentials if they were not set
    if not bool(hostname):
        hostname = input('Enter the hostname')
    if not bool(username):
        username = input('Enter the API username')
    if not bool(password):
        password = getpass.getpass('Enter the password')
    return


# Clear the screen and print information
os.system('clear')
print('Palo Alto REST API automation demo - W Embrey - ePlus')
print('\n *** WARNING - getpass doesnt work in Windows so make sure'
      ' you modify the script to add your password')

# use the XML api to gather the API key for the user.
def get_key():
    url = 'https://' + hostname + '/api/'
    querystring = {"type":"keygen","user":username,"password":password}
    response = requests.request("GET", url, params=querystring, verify=False)
    xml_response = xt.fromstring(response.text)
    apikey = xml_response[0][0].text
    return apikey

# this function will get a name for the input file
def get_inputfile():
    inputfile = input('\nEnter the file name for address entries:' \
    ' "address.txt": ')
    if not bool(inputfile):
        inputfile = 'address.txt'
        print(f'\nYou didn\'t enter a file name. We will use "address.txt"' \
        f' as the zone file.')
    return inputfile

def get_newaddresses(inputfile):

    # Check if zone conversion file was added and load it
    if bool(inputfile):
        try:
            f = open(inputfile, 'r')
            addressdata = f.read()
            addresslist = addressdata.split('\n')
            print(f'\n{len(addresslist)} lines read from file: ' \
            f'{inputfile}')
            f.close()
        except Exception as e:
            print(f'\nFile open of {inputfile} failed with error:\n{e}')
            sys.exit()

        x = 0 # start a line counter at 0
        #create the empty address dictionary with top level item
        address_dict = {}
        address_dict["entry"] = []

        # loop through the line entries
        for addressentry in addresslist:
            if not bool(addressentry):
                break
            try:
                line_dict = {}
                entrylist = addressentry.split(',')
                line_dict["@name"] = entrylist[0]
                line_dict["description"] = entrylist[1]
                line_dict["ip-netmask"] = entrylist[2]
                line_dict["tag"] = {"member":[]}
                try:
                    for item in entrylist[3:]:
                        line_dict["tag"]["member"].append(item)
                except:
                        pass
                address_dict["entry"].append(line_dict)
                x += 1 # increment the line counter for error finding
            except Exception as e:
                print(f'\nAdress file mapping failed for "{addressentry}" ' \
                f'at line {x} with error:\n{e}')
                sys.exit()
        print('\nSummary of address mappings')
        print(json.dumps(address_dict, indent=4))
        command = input(
            '\nIf these are wrong - press q to finish and start again or' \
            ' press [Enter] to continue: ')
        if str.lower(command) == 'q':
            sys.exit()
        return address_dict

# this function will get a list of addresses on the firewall
def get_addresses(apikey):
    url = 'https://' + hostname + '/restapi/9.0/Objects/Addresses'
    querystring = {"location":"vsys","vsys":"vsys1","key":apikey}
    response = requests.request("GET", url, verify=False, params=querystring)

    # process the response if it was a success
    if response.status_code is 200:

        # convert the bytes payload into a python dictionary
        json_data = response.json()

        # find the address entries and add to a list
        try:
            address_list = json_data['result']['entry']

            # count the number of address entries
            address_count = int(json_data['result']['@count'])
            print(f'\nConnection success. {str(address_count)} entries found')

            # loop through the addresses
            for address in address_list:
                try:
                    desc = address["description"]
                except:
                    desc = 'No description found'
                print(f'\n{address["@name"]} {address["ip-netmask"]}' \
                f' {desc}')
        except:
            print('No addresses found on firewall')

    # notify is the request did not response with 200
    else:
        print(f'Unable to process response. Status code {response.status_code}')


# this function will add an address to the firewall in vsys1
def set_address(apikey,address_dict):
    # loop through the dictionary
    for entry in address_dict["entry"]:
        payload = {}
        payload["entry"] = entry
        print(f'Adding {entry["@name"]}')

        # build the request
        url = "https://" + hostname + "/restapi/9.0/Objects/Addresses"
        querystring = {"name":entry["@name"],"location":"vsys","vsys":"vsys1", \
                       "key":apikey}
        response = requests.request("POST", url, verify=False, \
                                    json=payload, params=querystring)
        if response.status_code is 200:
            print(f'Request successfully sent')
        else:
            print(f'Update failed: {response.text}, {response.reason}')


# this is the standard starting point where you call the functions to begin
def main():
    global apikey

    # call the function to check credentials
    if not bool(apikey):
        print('We don\'t have an API Key yet')
        get_creds()
        print(f'\nCredentials confirmed')

        # call the function to get the API key
        apikey = get_key()
        print(f'Gathered API from {hostname}\nKey:{apikey}\n\n')
        input('Hit [Enter] to get addresses\n\n')

    # call the function to get the addresses
    get_addresses(apikey)

    inputfile = get_inputfile()
    address_dict = get_newaddresses(inputfile)

    # add the option to add the address entries
    command = input('\nAdd address entries to the firewall? (y/n)')
    if str.lower(command) != 'y':
        print('OK, closing script!')
        sys.exit()
    else:
        set_address(apikey,address_dict)
        print('Recap of current addresses on firewall')
        get_addresses(apikey)

    # exit the script
    print('All done, closing script!')
    sys.exit()


# this boilerplate function works if the script was called directly.
# if the script was imported into another script, it will wait to be called.
if __name__ == "__main__":
    main()
