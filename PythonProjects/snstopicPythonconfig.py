import boto3

sns.publish(
    TopicArn=SNS_TOPIC_ARN
    "Subject"="Update: New message received in SQS"
    )