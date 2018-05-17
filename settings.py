#  -*- coding: utf-8 -*-

from kombu import (
    Exchange,
    Queue
)
from celery.schedules import crontab


DEBUG = True
SECRET_KEY = 'a33c17a0-791c'
SQLALCHEMY_DATABASE_URI = "xxxx"
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_RECYCLE=60


BROKER_URL = "amqp://admin:admin@localhost:5672/zeus"
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'


CELERY_QUEUES = (
    Queue("default", routing_key='default'),
    Queue("video_download", Exchange("video_download", type='direct'), routing_key="video_download"),
    Queue("get_tasks", Exchange("get_tasks", type='direct'), routing_key="get_tasks")
)

CELERY_ROUTES = {
    'video_download': {"queue": "video_download", "routing_key": 'video_download'},
    'get_tasks': {"queue": "get_tasks", "routing_key": 'get_tasks'}
}

CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True

# CELERYD_TASK_SOFT_TIME_LIMIT = 30 * 60

CELERYBEAT_SCHEDULE = {
    'get_tasks': {
        'task': 'get_tasks',
        'schedule': crontab(hour="*/1", minute=40)
    }
}

DOWNLOAD_PATH = "/home/work/video"

