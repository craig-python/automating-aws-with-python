# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')

# Create a key pair
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)

get_ipython().run_line_magic('ls', '-l python_automation_key.pem')

import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')

# Find an AMI
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
ami_name = 'amzn-ami-hvm-2018.03.0.20180508-x86_64-gp2'
img = ec2.Image('ami-09d95fab7fff3776c')
img = ec2.Image('ami-0e9089763828757e1')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2'
ami_name = 'amzn-ami-hvm-2018.03.0.20200602.1-x86_64-gp2'
ami_name
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img

# Create an Instance
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName = key.key_name)
instances
ec2.Instance(id='i-01ed269c364f7c7c6')
inst = instances[0]
inst
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName = key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '94.4.107.253/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
