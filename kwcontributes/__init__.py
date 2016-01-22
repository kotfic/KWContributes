from __future__ import absolute_import
from celery import Celery

INCLUDES = (
    kwcontributes.github_archive
)

app = Celery('kwcontributes',
             backend='amqp',
             broker='amqp://guest:guest@localhost:5672',
             include=INCLUDES
)

app.config.update(
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_ACCEPT_CONTENT = ('json',),
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_ACKS_LATE = True,
    CELERYD_PREFETCH_MULTIPLIER = 1
)

if __name__ == '__main__':
    app.start()
