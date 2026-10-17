import json, boto3, base64, os

s3 = boto3.client("s3")
sfn = boto3.client("stepfunctions")

BUCKET = os.environ["BUCKET"]
STATE_MACHINE_ARN = os.environ["STATE_MACHINE_ARN"]

def is_admin(event):
    claims = event["requestContext"]["authorizer"]["claims"]
    groups = claims.get("cognito:groups", "")
    return "admin" in groups

# ---------- UPLOAD ----------
def upload(event, context):
    body = json.loads(event["body"])
    filename = body["filename"]
    filedata = base64.b64decode(body["file"])

    s3.put_object(Bucket=BUCKET, Key=filename, Body=filedata)

    resp = sfn.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        input=json.dumps({"filename": filename})
    )

    return {"statusCode":200,"body":json.dumps({"executionArn":resp["executionArn"]})}

# ---------- FILES ----------
def files(event,context):
    objs = s3.list_objects_v2(Bucket=BUCKET)
    return {"statusCode":200,"body":json.dumps({"files":[o["Key"] for o in objs.get("Contents",[])]})}

# ---------- DOWNLOAD ----------
def download(event, context):
    key = event["queryStringParameters"]["filename"]

    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": key},
        ExpiresIn=3600
    )

    return {"statusCode":200,"body":json.dumps({"url":url})}

# ---------- DELETE ----------
def delete(event, context):
    if not is_admin(event):
        return {"statusCode":403,"body":"Admin only"}

    body = json.loads(event["body"])
    s3.delete_object(Bucket=BUCKET, Key=body["filename"])
    return {"statusCode":200,"body":"deleted"}

# ---------- STATUS ----------
def status(event,context):
    body=json.loads(event["body"])
    desc=sfn.describe_execution(executionArn=body["executionArn"])
    return {"statusCode":200,"body":json.dumps({"status":desc["status"],"output":desc.get("output","")})}