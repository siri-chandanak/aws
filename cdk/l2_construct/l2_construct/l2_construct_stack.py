from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class L2ConstructStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # lambda api using L2 construct

        # Create a Lambda function
        lambda_function = _lambda.Function( 
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Create an API Gateway REST API resource backed by our "lambda_function"
        api = apigateway.LambdaRestApi(
            self, "L2ConstructApi",
            handler=lambda_function,
            proxy=False
        )   
        # Define a resource and method for the API
        items = api.root.add_resource("First")
        items.add_method("GET")  # GET /items
