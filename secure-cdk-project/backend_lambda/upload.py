import json
import boto3
import uuid
import os

s3 = boto3.client('s3')
sf = boto3.client('stepfunctions')

BUCKET = os.environ["BUCKET"]
STATE_MACHINE_ARN = os.environ["STATE_MACHINE_ARN"]

def handler(event, context):

    body = event.get("body", "empty")
    file_id = str(uuid.uuid4())

    s3.put_object(
        Bucket=BUCKET,
        Key=file_id,
        Body=body
    )

    exec = sf.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        input=json.dumps({"file_id": file_id})
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "file_id": file_id,
            "executionArn": exec["executionArn"]
        })
    }