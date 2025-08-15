import aws_cdk as core
import aws_cdk.assertions as assertions

from l1_construct.l1_construct_stack import L1ConstructStack

# example tests. To run these tests, uncomment this file along with the example
# resource in l1_construct/l1_construct_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = L1ConstructStack(app, "l1-construct")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
