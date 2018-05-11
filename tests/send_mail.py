from tests import tasks

tasks.sendmail.delay(dict(to='celery@python.org'))
