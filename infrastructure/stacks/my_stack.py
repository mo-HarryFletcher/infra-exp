from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct
from app_constants import NAME

class MyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            f"MyStackBucket-{NAME}",
            bucket_name=f"my-bucket-{NAME}",
            removal_policy=RemovalPolicy.DESTROY,
        )
