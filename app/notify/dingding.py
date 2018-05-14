from .base import Base
import requests
import json


class DingDing(Base):

    def __init__(self):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token={}'

    def send(self, msg, to):
        msg_type = 'text'
        data = self.get_msg_data(msg, msg_type)
        headers = {'content-type': 'application/json;charset=utf-8'}
        url = self.url.format(to)
        return requests.post(url, data=json.dumps(data), headers=headers)

    def get_msg_data(self, msg, msg_type):
        if msg_type == 'text':
            return self._text(msg)
        elif msg_type == 'markdown':
            return self._markdown(msg)
        elif msg_type == 'link':
            return self._link(msg)
        else:
            return self._text(msg)

    def _text(self, msg):
        return {'msgtype': 'text',
                'text': {'content': msg}
                }

    def _markdown(self, msg):
        return {"msgtype": "markdown",
                "markdown": {"title": msg[:10],
                             "text": msg
                             }
                }

    def _link(self, msg):
        return {"msgtype": "link",
                "link": {"text": msg,
                         "title": msg[:10],
                         "picUrl": "",
                         "messageUrl": 'http://www.baidu.com'
                         }
                }
