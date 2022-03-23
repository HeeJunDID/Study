from prefect import task


@task
def say_hello():
    print("Hello, world!")


@task
def add(x, y=1):
    return x + y
