import prefect
from prefect import Flow, task


@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, Cloud!")


with Flow("hello-flow") as flow:
    say_hello()

# Register the flow under the "tutorial" project
flow.register(project_name="tutorial")
