from flask import Flask
from celery import Celery
from time import sleep

app = Flask(__name__)

app.debug = True
app.config['CELERY_BROKER_URL'] = 'redis://123.207.152.86:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://123.207.152.86:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task()
def background_task(arg1, arg2):
    print('start....')
    sleep(2)
    print('end....')
    return arg1 + arg2


@app.route('/')
def index():
    task = background_task.delay(10, 20)
    print(task)
    return "hello"


if __name__ == '__main__':
    app.run()
