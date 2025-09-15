import json

def lambda_handler(event,context):
   
    print("Received event:", json.dumps(event))

    # Extract S3 object info if present event is saved as s3{bucket:{name:bucketname} object:{key:zipfilename}}
    s3_info = None
    if "s3" in event:
        bucket = event["s3"].get("bucket", {}).get("name")
        key = event["s3"].get("object", {}).get("key")
        if bucket and key:
            s3_info = f"s3://{bucket}/{key}"
            print(f"Deployed package version: {s3_info}")

    # Business logic response
    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Lambda Triggered",
            "deployed_package": s3_info if s3_info else "N/A"
        })
    }

    return result
