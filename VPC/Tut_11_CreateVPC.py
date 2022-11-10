#tutorial 11
#How to create VPC using python and boto3
import boto3
client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.0.0.2/16')

