#Tutorial 23: create or launch an EC2 instance using python/boto3:
import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)
