# errorhandler.py
def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print(message)