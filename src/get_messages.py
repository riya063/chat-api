import os
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    print("EVENT:", json.dumps(event))
    try:
        response = table.scan()
        messages = response.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(messages)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
