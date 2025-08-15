import aws_cdk as core
import aws_cdk.assertions as assertions

from s3stack.s3_stack import MultistackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in multistack/multistack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MultistackStack(app, "multistack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
