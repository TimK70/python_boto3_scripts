import logging
import json
import boto3
import time
from botocore.exceptions import ClientError
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)

def create_topic(name):
    """
    Creates a modification topic.ArithmeticError
    :param name: The name of the topic to create.
    :return: The newly created topic.
    """
    sns_client = boto3.client('sns', verify=False)
    
    try:
        topic = sns_client.create_topic(Name=name)
        logger.info("Created topic %s with ARN %s.", name, topic['TopicArn'])
        
    except ClientError:
        logger.exception("Couldn't create topic %s.", name)
        raise
    else:
        return topic

if __name__ == '__main__':
    topic_name = f'errormessage{time.time_ns()}'
    print(f"Creating topic {topic_name}.")
    topic = create_topic(topic_name)