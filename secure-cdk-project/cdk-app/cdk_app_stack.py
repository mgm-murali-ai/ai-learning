from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
)
from constructs import Construct

class SecureFileStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # S3 bucket
        bucket = s3.Bucket(self, "FileBucket")

        # Lambda to process file
        process_fn = _lambda.Function(
            self, "ProcessFn",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="process.handler",
            code=_lambda.Code.from_asset("../backend_lambda")
        )

        # Upload Lambda
        upload_fn = _lambda.Function(
            self, "UploadFn",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="upload.handler",
            code=_lambda.Code.from_asset("../backend_lambda"),
            environment={
                "BUCKET": bucket.bucket_name,
                "STATE_MACHINE_ARN": "dummy"  # updated later
            }
        )

        bucket.grant_read_write(upload_fn)
        bucket.grant_read_write(process_fn)

        # Step Function
        task = tasks.LambdaInvoke(
            self, "InvokeProcessor",
            lambda_function=process_fn,
            output_path="$.Payload"
        )

        definition = task

        sm = sfn.StateMachine(
            self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(definition)
        )

        # Update env with real ARN
        upload_fn.add_environment("STATE_MACHINE_ARN", sm.state_machine_arn)

        # API Gateway
        api = apigw.RestApi(self, "SecureApi")

        upload_integration = apigw.LambdaIntegration(upload_fn)

        api.root.add_resource("upload").add_method(
            "POST",
            upload_integration,
            api_key_required=True
        )

        # API Key + Usage plan
        key = api.add_api_key("ApiKey")
        plan = api.add_usage_plan("UsagePlan")

        plan.add_api_key(key)
        plan.add_api_stage(stage=api.deployment_stage)