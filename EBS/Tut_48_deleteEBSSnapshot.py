#Tutorial 48: how to delete aws ebs volume snapshot using boto3 python
import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-05017222842e31cf7')