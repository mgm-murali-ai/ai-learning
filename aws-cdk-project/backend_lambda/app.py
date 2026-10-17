import json
import boto3
import os
import base64

s3 = boto3.client("s3")
BUCKET = os.environ["BUCKET"]

def handler(event, context):

    body = json.loads(event["body"])

    filename = body["filename"]
    content = body["content"]

    file_bytes = base64.b64decode(content)

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=file_bytes
    )

    return {
        "status": "uploaded",
        "file": filename
    }