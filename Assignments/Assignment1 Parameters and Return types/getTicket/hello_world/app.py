import json
import logging
import uuid
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_payment_details(payment_details):
    required_fields = ["name", "credit_card_number", "expiry_date"]
    missing_fields = [field for field in required_fields if field not in payment_details]

    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    expiry_date = payment_details["expiry_date"]
    try:
        datetime.strptime(expiry_date, "%m/%y")
    except ValueError:
        raise ValueError("Invalid expiry date format. Use MM/YY.")


def generate_ticket():
    ticket = {
        "ticket_id": str(uuid.uuid4()),
        "type": "movie",
        "issued_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": {
            "seat": "A12",
            "screen": 3,
            "time": "7:30 PM",
            "movie": "Avengers: Endgame"
        }
    }
    return ticket


def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        validate_payment_details(body)

        ticket = generate_ticket()

        logger.info(f"Payment received for {body['name']}. Ticket issued: {ticket['ticket_id']}")

        return {
            "statusCode": 200,
            "body": json.dumps(ticket)
        }

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
