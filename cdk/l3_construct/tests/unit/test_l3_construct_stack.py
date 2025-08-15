import aws_cdk as core
import aws_cdk.assertions as assertions

from l3_construct.l3_construct_stack import L3ConstructStack

# example tests. To run these tests, uncomment this file along with the example
# resource in l3_construct/l3_construct_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = L3ConstructStack(app, "l3-construct")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
