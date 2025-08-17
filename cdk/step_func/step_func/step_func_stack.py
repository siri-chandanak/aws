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

        #create a choice state 
        #if input is integer, go to task1, else if input is string, go to task2, else go to fail state
        #from task1 and task2, go to success state and then end the state machine
        
        success_state = sfn.Succeed(self, "SuccessState")
        
        fail_state = sfn.Fail(self, "FailState", error="InvalidInput", cause="Input must be a number or a string")
        
        choice_state = sfn.Choice(self, "ChoiceState") \
            .when(sfn.Condition.is_numeric("$.input"), 
                tasks.LambdaInvoke(self, "Task1",
                lambda_function=lambda_function1,
                output_path="$.Payload"
            ).next(success_state)) \
            .when(sfn.Condition.is_string("$.input"), 
                tasks.LambdaInvoke(self, "Task2",
                lambda_function=lambda_function2,
                output_path="$.Payload"
            ).next(success_state)) \
            .otherwise(fail_state) 
        
        # Define the state machine, starting with the choice state
        
        state_machine_definition = choice_state
        state_machine = sfn.StateMachine(self, "StateMachine",
                                         definition_body=sfn.DefinitionBody.from_chainable(state_machine_definition),
)


