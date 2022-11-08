import boto3
s3_resource=boto3.client("s3")
#s3_resource.delete_object(Bucket='week14testbucket3',
#    Key='GOPR0021.JPG')

import os
import glob

objects=s3_resource.list_objects(Bucket='week14testbucket3')["Contents"]
len(objects)
for object in objects:
    response=s3_resource.delete_object(Bucket='week14testbucket3',
    Key=object["Key"])
    print(response)