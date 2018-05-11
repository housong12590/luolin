from celery import Celery

broker = 'redis://123.207.152.86:6379/0'
backend = 'redis://123.207.152.86:6379/1'

celery = Celery('tasks', broker=broker, backend=backend)


@celery.task
def add(x, y):
    return x + y
