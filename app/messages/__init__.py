import importlib


def send_msg(msg):
    setting = ['app.messages.email.Email', 'app.messages.dingding.DingDing']
    for path in setting:
        module, cls = path.rsplit('.', maxsplit=1)
        module = importlib.import_module(module)
        obj = getattr(module, cls)()
        obj.send(msg)
