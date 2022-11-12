#how to create aws ebs volume from snapshot using boto3 and python:
import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1d',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-05017222842e31cf7',
    VolumeType='gp2')