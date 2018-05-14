import importlib
from flask import current_app as app

# from app import celery

__obj_path = {
    'email': 'app.notify.email.Email',
    'dingding': 'app.notify.email.Email'
}


def send_msg(msg):
    path = __obj_path.get(app.config['NOTIFY_TYPE'], None)
    module, cls = path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module)
    obj = getattr(module, cls)()
    for recipient in app.config['RECIPIENTS']:
        __send_async_msg(obj, msg, recipient)


# @celery.task
def __send_async_msg(obj, msg, to):
    obj.send(msg, to)
