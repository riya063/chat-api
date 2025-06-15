import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))
    body = json.loads(event['body'])
    message_id = body['messageId']

    table.delete_item(Key={'messageId': message_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Message deleted'})
    }
