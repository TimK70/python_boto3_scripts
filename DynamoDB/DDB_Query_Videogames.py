import boto3
import json
from boto3.dynamodb.conditions import Key

TABLE_NAME = "Favorite_Video_Games"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
print(table)


response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression=Key('Genre = :Genre'),
    ExpressionAttributeValues={':Genre': {'S': 'Pitfall'}
    }
)
print(response['Items'])
#from boto3.dynamodb.conditions import Key #allows us to call the query

#dynamodb = boto3.resource('dynamodb') #reference the boto3 DynamoDB resource.

#table = dynamodb.Table('Favorie_Video_Games')

#response = table.query(
#  KeyConditionExpression=Key('Genre').eq('Sports')
#)
#print(response['Items'])