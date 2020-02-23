from .app import BROKER_HOST_NAME

BROKER_URL = 'redis://{}:6379/0'.format(BROKER_HOST_NAME)
CELERY_RESULT_BACKEND = 'redis://{}:6379/0'.format(BROKER_HOST_NAME)

# BROKER_URL = f"amqp://rmxuser:rmxpass@{BROKER_HOST_NAME}:5672/rmxvhost"
# CELERY_RESULT_BACKEND = 'rpc://'

CELERY_IMPORTS = ('rmxnmf.task', )

CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ROUTES = {

    'rmxnmf.task.*': {'queue': 'rmxnmf'},

}

