import aws_cdk as core
import aws_cdk.assertions as assertions

from l2_construct.l2_construct_stack import L2ConstructStack

# example tests. To run these tests, uncomment this file along with the example
# resource in l2_construct/l2_construct_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = L2ConstructStack(app, "l2-construct")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
