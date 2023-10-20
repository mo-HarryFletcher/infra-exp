import aws_cdk as core
import aws_cdk.assertions as assertions

from infra_exp.infra_exp_stack import InfraExpStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra_exp/infra_exp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfraExpStack(app, "infra-exp")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
