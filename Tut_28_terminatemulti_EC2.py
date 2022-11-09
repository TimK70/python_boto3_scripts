#Tutorial 28: Terminate multiple EC2 instances using boto3 python
import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]
li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        if instance_id != "i-0a9c8ffec4d7e314e":
            li.append(instance_id)
ec2_client.terminate_instances(InstanceIds=li)

