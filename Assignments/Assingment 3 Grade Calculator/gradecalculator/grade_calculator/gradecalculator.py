import boto3
import json
import os

s3 = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    topic = os.environ.get('GRADE_CALCULATOR_TOPIC')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read().decode('utf-8')
    checkout_events = json.loads(file_content)
    for each_event in checkout_events:
        score = each_event["score"]
        match score:
            case score if 60 < score <= 70:
                grade = "B"
            case score if score <= 70:
                grade = "A"
            case _:
                grade = "C"
        message = json.dumps({"name": each_event["name"],
                              "grade": grade
                              })
        sns_client.publish(
            TopicArn=topic,
            Message=json.dumps({'default': message}),
            MessageStructure='json'
        )


