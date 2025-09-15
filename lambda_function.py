def lambda_handler(event, context):
    print("Incoming event:", json.dumps(event))
    s3_info = None
    try:
        record = event["Records"][0]
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        s3_info = f"{bucket}/{key}"
    except Exception as e:
        print(f"Error parsing event: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Lambda Triggered",
            "deployed_package": s3_info if s3_info else "N/A"
        })
    }
