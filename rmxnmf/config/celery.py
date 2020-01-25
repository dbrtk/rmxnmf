from .app import REDIS_HOST_NAME

BROKER_URL = 'redis://{}:6379/0'.format(REDIS_HOST_NAME)
CELERY_RESULT_BACKEND = 'redis://{}:6379/0'.format(REDIS_HOST_NAME)

CELERY_IMPORTS = ('rmxnmf.task', )

CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ROUTES = {

    'rmxnmf.task.*': {'queue': 'rmxnmf'},

}

RMXBOT_TASKS = {

    'nlp_callback': 'rmxbot.tasks.container.nlp_callback_success',

    'integrity_check_callback': 'rmxbot.tasks.container.integrity_check_callback',

}
