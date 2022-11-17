import boto3      #Need this SDK for Python to interact with AWS
sqs = boto3.resource('sqs')      #The SQS Resources manage the SQS feature
queue = sqs.create_queue(QueueName='MySQS_Time')     #Creates a queue and names it MySQS_Time
print(queue.url)      #to get the queue url