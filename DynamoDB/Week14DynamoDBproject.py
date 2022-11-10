import boto3  #imports the SDK for Python from AWS

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='*****',
    aws_secret_access_key='*****',
    )
    
    
    
    
    
    
    
    #!/usr/bin/env python3.9  #This tells my file I'm using python. Its similar to a bash script
                          #Allows mo also use "./" instead of calling on python
import boto3  #Imports boto3, the SDK for python from AWS

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  #this will make a variable named DynamoDB thats calls the dynamodb resource of boto3

table = dynamodb.create_table(     #Creates our table, this is from the boto3 libary that calls the create_table 
    TableName='Federation',   #Give your table a name
    KeySchema=[    #Key schema required by dynamodb, 
        {
            'AttributeName': 'PlanetName',  #Name of your part. key
            'KeyType': 'HASH'  #Partition key  is a must
        },
        {
            'AttributeName': 'Quadrant',   #Name of sort key
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PlanetName',    #Reenter your part. key and is its a S|N|B, string, number, boolean
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Quadrant', #Reenter your sort key and is its a S|N|B, string, number, boolean
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={    #This is how fast your table will upload data
        'ReadCapacityUnits': 1,  #if you have alot of info to upload make it like 10 RCU/WCUI
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)  #Will print that our table is creating 