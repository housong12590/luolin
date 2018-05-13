from flask import current_app


def send_async_email(app, msg):
    pass


from app.messages import send_msg

send_msg("你好啊")
