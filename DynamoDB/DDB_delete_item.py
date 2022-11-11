import boto3
dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_item(
    TableName='Favorite_Video_Games',
    Key=  {
        'Title': {"S": "NHL 22"}, 
        "Genre": {"S": "Sports"},
        }
)