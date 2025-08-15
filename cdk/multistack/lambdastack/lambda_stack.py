from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.handler",
            code=_lambda.Code.from_inline(
                "def handler(event, context):\n"
                "    return {'statusCode': 200, 'body': 'Hello from Lambda!'}"
            )
        )
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MultistackQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
