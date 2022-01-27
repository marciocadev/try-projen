import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

from try_projen.try_projen_stack import MyStack

@pytest.fixture(scope='module')
def template():
  app = App()
  stack = MyStack(app, "my-stack-test")
  template = Template.from_stack(stack)
  yield template


def test_cdk_metadata(template):
  template.find_resources("AWS::CDK::Metadata")
