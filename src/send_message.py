import json
import os
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    try:
        print("🟡 Event received:", json.dumps(event))

        body = json.loads(event.get("body", "{}"))

        # Ensure required fields exist
        if "username" not in body or "message" not in body:
            raise ValueError("Missing 'username' or 'message' in request body")

        id = str(uuid.uuid4())
        item = {
            "id": id,  # ⚠️ Make sure this matches your table's partition key
            "username": body["username"],
            "message": body["message"],
            "timestamp": datetime.utcnow().isoformat()
        }

        print("🟢 Writing item to DynamoDB:", item)
        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Message sent!", "id": id})
        }

    except Exception as e:
        print("🔴 Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
