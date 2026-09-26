# AWS SQS → Lambda Message Processor

A serverless AWS project demonstrating how Amazon SQS can trigger an AWS Lambda function to process messages, with Amazon CloudWatch used to verify execution and logging.

## Architecture

```text
Amazon SQS
    |
  Message
    ↓
AWS Lambda
    |
Process message
    ↓
Amazon CloudWatch Logs
```

## AWS Services Used

- **Amazon SQS** — Message queue
- **AWS Lambda** — Serverless message processing
- **Amazon CloudWatch** — Logging and monitoring
- **AWS IAM** — Permissions for Lambda to access SQS

## What I Built

- Created an Amazon SQS Standard queue.
- Created a Python AWS Lambda function.
- Configured an SQS event source trigger for the Lambda function.
- Configured the Lambda execution role with the required SQS permissions.
- Sent a test message to the SQS queue.
- Lambda automatically received and processed the message.
- Verified the message processing through Amazon CloudWatch Logs.

## Lambda Function

The Lambda function reads messages from the SQS event and prints the message body to CloudWatch.

```python
def lambda_handler(event, context):
    for record in event["Records"]:
        print("Received message:", record["body"])

    return {
        "processed": len(event["Records"])
    }
```

## Evidence

1. Amazon SQS Queue
2. Lambda Function
3. SQS → Lambda Trigger
4. Lambda Function Code
5. CloudWatch Message Processing

The screenshots are available in the [`screenshots`](screenshots/) directory.

## Key Concepts Practiced

- Serverless architecture
- Event-driven architecture
- Amazon SQS
- AWS Lambda
- Lambda event source mappings
- IAM execution roles and permissions
- CloudWatch logging
- Message-based processing
- AWS Console configuration
- Python Lambda functions

## Project Outcome

Successfully configured an event-driven workflow where a message placed into an Amazon SQS queue automatically triggers an AWS Lambda function, with the resulting execution verified through Amazon CloudWatch Logs.
