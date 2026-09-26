def lambda_handler(event, context):
    for record in event["Records"]:
        print("Received message:", record["body"])

    return {
        "processed": len(event["Records"])
    }
