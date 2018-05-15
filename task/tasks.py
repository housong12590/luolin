from flask import Flask
from celery import Celery, Task
from time import sleep

app = Flask(__name__)

app.debug = True
app.config['CELERY_BROKER_URL'] = 'redis://123.207.152.86:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://123.207.152.86:6379/0'
app.config['USER_OPTIONS'] = ''
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


class MyTask(Task):
    def run(self, *args, **kwargs):
        print('runing......')
        pass

    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0} on_success'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0} on_failure'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@celery.task()
def tasks(arg1, arg2):
    print('start....')
    sleep(2)
    print('end....')
    return arg1 + arg2


@celery.task(base=MyTask)
def tasks1():
    sleep(2)
    print('----------')
    return 10, 20


@app.route('/')
def index():
    task = tasks.delay(10, 20)
    print(task.id, task.status)
    return "hello"


@app.route('/task')
def tasks12():
    task = tasks1.apply_async()
    return task.id


def result():
    print('任务完成')


import os
from threading import Thread


def start_task():
    os.system('celery -A tasks:celery worker --loglevel=info --pool=solo')


if __name__ == '__main__':

    Thread(target=start_task).start()

    app.run()
