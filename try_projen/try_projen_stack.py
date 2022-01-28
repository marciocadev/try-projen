from aws_cdk import RemovalPolicy, Stack
from aws_cdk.aws_s3 import Bucket
from constructs import Construct


class MyStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    Bucket(self, "teste2", removal_policy=RemovalPolicy.DESTROY)

