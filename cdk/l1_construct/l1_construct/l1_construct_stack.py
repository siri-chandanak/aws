from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_iam as iam
)
from constructs import Construct

class L1ConstructStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        lambda_role = iam.Role.from_role_arn(
            self, "ImportedLambdaRole",
            "arn:aws:iam::339712964114:role/LambdaApi"
        )

        # Create a Lambda function
        lambda_function = _lambda.Function(
            self, "LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            role=lambda_role
        )

        # Create an API Gateway REST API
        api = apigateway.CfnRestApi(
            self, "L1ConstructApi",
            name="L1ConstructApi",
            description="API for L1 Construct Stack",
            endpoint_configuration=apigateway.CfnRestApi.EndpointConfigurationProperty(
                types=["REGIONAL"]
            )  
        )

        # Add a resource to the API
        resource1 = apigateway.CfnResource(
            self, "Resource1",
            parent_id=api.attr_root_resource_id,
            path_part="First",
            rest_api_id=api.ref
        )       

        # Add GET method to the resource
        method1=apigateway.CfnMethod(
            self, "method1",
            rest_api_id=api.ref,
            resource_id=resource1.ref,
            http_method="GET",
            authorization_type="NONE",
            integration=apigateway.CfnMethod.IntegrationProperty(
                integration_http_method="POST",
                type="AWS_PROXY",
                uri=f"arn:aws:apigateway:{self.region}:lambda:path/2015-03-31/functions/{lambda_function.function_arn}/invocations"
            )
        )
        # Grant API Gateway permission to invoke Lambda function
        p = _lambda.CfnPermission(
            self, "ApiGatewayInvokePermission",
            action="lambda:InvokeFunction",
            function_name=lambda_function.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"arn:aws:execute-api:{self.region}:{self.account}:{api.ref}/*/GET/First"        
        )
        
        
       # Deploy the API
        dep = apigateway.CfnDeployment(
            self, "Deployment",
            rest_api_id=api.ref,
        )

        dep.add_dependency(method1)

        stage = apigateway.CfnStage(
            self, "Stage",
            rest_api_id=api.ref,    
            deployment_id=dep.ref,
            stage_name="prod"
        )






        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "L1ConstructQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
