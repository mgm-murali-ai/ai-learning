import json
from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigateway as apigw,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
)

from pathlib import Path


class SecureFileStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # ---------------- S3 BUCKET ----------------
        bucket = s3.Bucket(self, "UploadBucket")

        # ---------------- LAMBDA ----------------
        lambda_path = str(Path(__file__).resolve().parent.parent / "backend_lambda")

        fn = _lambda.Function(
            self, "Handler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="app.handler",
            code=_lambda.Code.from_asset(lambda_path),
            environment={
                "BUCKET": bucket.bucket_name
            }
        )

        bucket.grant_put(fn)

        # ---------------- STEP FUNCTION ----------------
        task = tasks.LambdaInvoke(
            self, "ProcessFile",
            lambda_function=fn,
            output_path="$.Payload"
        )

        definition = task

        state_machine = sfn.StateMachine(
            self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(definition)
        )

        # ---------------- API GATEWAY ----------------
        api = apigw.RestApi(self, "SecureApi")

        # Role for API Gateway to call Step Function
        apigw_role = iam.Role(
            self, "ApiGatewayStepFnRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com")
        )

        state_machine.grant_start_execution(apigw_role)

        # ---------------- /upload endpoint ----------------
        upload = api.root.add_resource("upload")

        upload.add_method(
            "POST",
            apigw.AwsIntegration(
                service="states",
                action="StartExecution",
                integration_http_method="POST",
                options=apigw.IntegrationOptions(
                    credentials_role=apigw_role,
                    request_templates={
                        "application/json": json.dumps({
                            "input": "$util.escapeJavaScript($input.body)",
                            "stateMachineArn": state_machine.state_machine_arn
                        })
                    },
                    integration_responses=[{"statusCode": "200"}],
                ),
            ),
            method_responses=[{"statusCode": "200"}],
            api_key_required=True
        )

        # ---------------- API KEY + USAGE PLAN ----------------
        plan = api.add_usage_plan("UsagePlan")

        key = api.add_api_key("ApiKey")

        plan.add_api_key(key)

        plan.add_api_stage(stage=api.deployment_stage)

        # ---------------- OUTPUTS ----------------
        cdk.CfnOutput(self, "ApiUrl", value=api.url)
        cdk.CfnOutput(self, "BucketName", value=bucket.bucket_name)
        cdk.CfnOutput(self, "StateMachineArn", value=state_machine.state_machine_arn)