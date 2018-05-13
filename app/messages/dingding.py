from .base import Base


class DingDing(Base):

    def send(self, msg):
        print(msg, 'ding')
