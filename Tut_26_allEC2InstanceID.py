#Tutorial 26: get all EC2 Instance ID using python/boto3
import boto3

ec2_client=boto3.client("ec2")
response=ec2_client.describe_instances()
data=["Reservations"][0],[1]
data_instance=data["Instances[]"

for i in range(data_instance):
    print(f"instance id is {data_instance[i]['InstanceId']}")
