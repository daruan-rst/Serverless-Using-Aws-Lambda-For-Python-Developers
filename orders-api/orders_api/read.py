import json


def lambda_handler(event, context):
    order = {
        "id": 123,
        "itemName": "Mac Book Pro",
        "quantity": 100
    }
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(order)
    }
