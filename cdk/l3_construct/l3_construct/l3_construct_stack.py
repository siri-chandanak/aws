from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

from aws_solutions_constructs import (
    aws_apigateway_lambda as apigateway_lambda)


class L3ConstructStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # lambda and API using L3 constructs

        lambda_api = apigateway_lambda.ApiGatewayToLambda(
            self, 'LambdaApi',
            lambda_function_props={
                'runtime': _lambda.Runtime.PYTHON_3_9,
                'code': _lambda.Code.from_asset('lambda'),
                'handler': 'index.lambda_handler'
            },
            api_gateway_props=apigateway.RestApiProps(
                rest_api_name='MyLambdaApi',
                description='This is a sample API Gateway integrated with Lambda',
                default_method_options=apigateway.MethodOptions(
                    authorization_type=apigateway.AuthorizationType.NONE
            )
            )
        )




