from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="marciocadev@gmail.com",
    author_name="Marcio Cruz de Almeida",
    cdk_version="2.1.0",
    module_name="try_projen",
    name="try-projen",
    version="0.1.0",
)

project.synth()