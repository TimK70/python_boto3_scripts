#Tutorial 12: how to describe vpc using python/boto3
import boto3
client=boto3.client("ec2")

#how to describe all vpc's available in your account
x=client.describe_vpcs()
no_of_vpcs=x['Vpcs']
len(no_of_vpcs)
for vpc in no_of_vpcs:
    print(vpc["VpcId"])

#How to describe one vpc based on vpc id

