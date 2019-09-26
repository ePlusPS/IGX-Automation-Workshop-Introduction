#!/usr/bin/env python

# import the modules we need
import boto3
import sys

# set the variable for owner_tag and the command
owner_tag = ''
command  = ''

# check if two arguments were passed to the cli
if len(sys.argv) < 3:
    print(f'Please provide an owner tag and command:\n "aws [owner] [start|stop|check]"')
    sys.exit()
else:
    try: # fail gracefully if the arguments are not present
        owner_tag = sys.argv[1]
        command = sys.argv[2]
    except:
        print('Unable to set variables')
        sys.exit()

# create the aws ec2 client
ec2 = boto3.client('ec2')

# Set the filter using the owner name
filters = [{'Name': 'tag:owner', 'Values': [owner_tag]}]

# get the instances information which will be in dictionary json format
get_instances = ec2.describe_instances(Filters = filters)

# create a list called my_instances from the list inside the dictionary
my_instances = get_instances['Reservations'][:]

# create the empty list and dictionary
my_status = {}
my_amids = []

# loop through the instances and look for the instance-id
for instance in my_instances:
    amid = instance['Instances'][0]['InstanceId'] # get the instance-id
    my_amids.append(amid) # add it to the list
    # add the instance-id and state to a disctionary pair
    my_status[amid] = [instance['Instances'][0]['State']['Name']]
    try:
        pub_ip = instance['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']
    except:
        pub_ip = 'No public IP'
    my_status[amid].append(pub_ip)
print(my_status)

# check if a valid command was given
if command == 'start':
    result = ec2.start_instances(InstanceIds=my_amids)
    print(result)
elif command == 'stop':
    result = ec2.stop_instances(InstanceIds=my_amids)
    print(result)
