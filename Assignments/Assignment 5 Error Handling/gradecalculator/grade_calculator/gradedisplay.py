#gradedisplay.py

import logging

logger = logging.getLogger('gradedisplay')
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    name = message["name"]
    grade = message["grade"]
    logger.info(f"{name}'s grade is {grade}")