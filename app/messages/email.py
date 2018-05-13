from .base import Base


class Email(Base):
    def send(self, msg):
        print(msg)
