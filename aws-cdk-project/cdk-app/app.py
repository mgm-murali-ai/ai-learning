#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_app_stack import SecureFileStack

app = cdk.App()
SecureFileStack(app, "SecureFileStack")
app.synth()