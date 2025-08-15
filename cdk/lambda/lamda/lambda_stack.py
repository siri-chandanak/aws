from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_function= lambda_.Function(
            self, "MyLambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_8,       
            handler="index.handler",
            code=lambda_.Code.from_inline(
                "import json\n"
                "def handler(event, context):\n"
                "    n=event.get('name', 'World')\n"
                "    return {'statusCode': 200, 'body': n+' from Lambda!'}"
            )
        )
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "LambdaQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
