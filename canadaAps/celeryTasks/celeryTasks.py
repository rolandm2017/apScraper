from time import sleep
from celery import current_app


@current_app.task(name="delayed_math")
def delayed_mathsss(x):
    sleep(x / 10)
    return x + 100

