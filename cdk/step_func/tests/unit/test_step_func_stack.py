import aws_cdk as core
import aws_cdk.assertions as assertions

from step_func.step_func_stack import StepFuncStack

# example tests. To run these tests, uncomment this file along with the example
# resource in step_func/step_func_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StepFuncStack(app, "step-func")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
