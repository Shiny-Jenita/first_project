import json
def lambda_handler(event,context):
    # Example: log the event
    print("Received event:", json.dumps(event))

    # Business logic goes here
    result = {
        "statusCode": 200,
        "body": json.dumps({"message": "Lambda Triggered ..."})
    }

    return result