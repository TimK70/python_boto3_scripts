import boto3
dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_item(
    TableName='Favorite_Video_Games', #item we want to delete
    Key=  {
        'Title': {"S": "NHL 22"}, #title and genre strings of item to delete from table.
        "Genre": {"S": "Sports"},
        }
)