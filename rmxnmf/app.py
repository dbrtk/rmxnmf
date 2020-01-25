
from celery import Celery

from rmxnmf.config import celery as celeryconf

celery = Celery('rmxnmf')

celery.config_from_object(celeryconf)

