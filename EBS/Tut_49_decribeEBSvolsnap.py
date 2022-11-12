#Tutorial 49: how to describe aws ebs volume snapshot using boto3 and python.
import boto3
ec2_client=boto3.client("ec2")
ec2_client.describe_snapshots(SnapshotIds=[
    'snap-07bd5ab0653d20ed9'])