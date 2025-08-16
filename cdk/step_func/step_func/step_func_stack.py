from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks
)
from constructs import Construct

class StepFuncStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Step Functions 

        # Define a Lambda function1
        lambda_function1 = _lambda.Function(
            self, "LambdaFunction1",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="numbers.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )
        # Define a Lambda function2
        lambda_function2 = _lambda.Function(
            self, "LambdaFunction2",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="strings.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Define a Step Function task for the first Lambda function
        task1 = tasks.LambdaInvoke(
            self, "Task1",
            lambda_function=lambda_function1,
            output_path="$.Payload"
        )   
        # Define a Step Function task for the second Lambda function
        task2 = tasks.LambdaInvoke(            self, "Task2",
            lambda_function=lambda_function2,
            output_path="$.Payload"
        )       
        # Define the Step Function state machine
        definition = task1.next(task2)  
        state_machine = sfn.StateMachine(
            self, "StateMachine",
            definition=definition
        )



        # example resource
        # queue = sqs.Queue(
        #     self, "StepFuncQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
