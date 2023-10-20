from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
    RemovalPolicy,
    aws_lambda,
)
from constructs import Construct
from app_constants import NAME

class MyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        queue = sqs.Queue(
            self,
            f"MyStackQueue-{NAME}",
            queue_name=f"my-queue-{NAME}",
            visibility_timeout=Duration.seconds(60)
        )

        bucket = s3.Bucket(
            self,
            f"MyStackBucket-{NAME}",
            bucket_name=f"my-bucket-{NAME}",
            removal_policy=RemovalPolicy.DESTROY,
        )

        lambda_function = aws_lambda.Function(
            self,
            f"MyStackFunction-{NAME}",
            function_name=f"my-function-{NAME}",
            code=aws_lambda.Code.from_asset("src/lambda/queue_to_bucket_lambda"),
            handler="main.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_10,
        )
