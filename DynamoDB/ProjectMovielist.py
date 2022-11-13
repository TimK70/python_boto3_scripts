import boto3

dynamodb = boto3.resource('dynamodb')  #DynamoDB variable created that will call boto3's dynamoDB's resource.

Video_Games = [    #List for our table:
    {'Title': "Need for Speed: Hot Pursuit", "Genre":"Action"},
    {'Title': "World of Warcraft", "Genre": "MMORPG"},
    {'Title': "Guild Wars", "Genre": "MMORPG"},
    {'Title': "NHL 22", "Genre": "Sports"},
    {'Title': "Horizon Zero Dawn", "Genre": "RPG"},
    {'Title': "Zork", "Genre": "Text Adventure"},
    {'Title': "Pitfall", "Genre": "Arcade"},
    {'Title': "PGA Tour 2K21", "Genre": "Sports"},
    {'Title': "Overwatch 2", "Genre": "eSports"},
    {'Title': "Tom Clancy's The Division 2", "Genre": "FPS"},
        ]
    
table = dynamodb.Table("Favorite_Video_Games") #Creates a variable, table, that calls our table name
with table.batch_writer() as batch:   #Batch writer that uploads multiple items to the DynamoDB
    for Title in Video_Games:
        batch.put_item(
            Item=Title
            )
