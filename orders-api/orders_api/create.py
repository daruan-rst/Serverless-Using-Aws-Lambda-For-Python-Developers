import json
import boto3
import os


def lambda_handler(event, context):
    order = json.loads(event['body'])
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ORDER_TABLE')

    table = dynamodb.Table(table_name)
    table.put_item(TableName=table, Item=order)
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }
