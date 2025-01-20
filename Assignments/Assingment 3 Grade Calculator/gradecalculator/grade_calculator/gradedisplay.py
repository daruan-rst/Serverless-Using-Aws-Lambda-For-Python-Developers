def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    name = message["name"]
    grade = message["grade"]
    print(f"{name}'s grade is {grade}")