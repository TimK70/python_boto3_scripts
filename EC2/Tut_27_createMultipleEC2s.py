# Tutorial 27: how to create multiple EC2 instances
import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3)