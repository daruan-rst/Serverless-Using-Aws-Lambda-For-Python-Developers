import asyncio
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

async def process_location(lat, lon):
    await asyncio.sleep(1)
    logger.info(f"Received coordinates: Latitude={lat}, Longitude={lon}")
    return {"message": "Coordinates logged successfully"}

def handler(event, context):
    try:
        # Parse input
        body = json.loads(event["body"])
        latitude = body.get("latitude")
        longitude = body.get("longitude")

        if latitude is None or longitude is None:
            raise ValueError("Latitude and Longitude must be provided.")

        response = process_location(latitude, longitude)

        return {
            "statusCode": 200,
            "body": json.dumps(response)
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
