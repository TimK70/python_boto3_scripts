#Tutorial22: removing VPC using python
import boto3
client=boto3.client("ec2")
response=client.delete_vpc(
    VpcId='vpc-05ab343304b0c0abc'
)
print(response)