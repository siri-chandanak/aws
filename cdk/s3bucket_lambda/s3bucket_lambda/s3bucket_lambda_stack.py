from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as _lambda,
)
from constructs import Construct

class S3BucketLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket=s3.Bucket(
            self, "MyS3Bucket",
            versioned=True,
        )
        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=_lambda.Code.from_inline(
                "def handler(event, context):\n"
                "    print('Event:', event)\n"
                "    return {'statusCode': 200, 'body': 'Hello from Lambda!'}"
            ),
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }   
        )
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "S3BucketLambdaQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
