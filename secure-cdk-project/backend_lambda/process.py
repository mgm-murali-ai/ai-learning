def handler(event, context):
    file_id = event["file_id"]

    return {
        "message": f"File {file_id} processed successfully"
    }