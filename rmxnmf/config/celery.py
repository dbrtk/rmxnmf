
from .app import RPC_HOST, RPC_PASS, RPC_PORT, RPC_USER, RPC_VHOST

# broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
_url = f'amqp://{RPC_USER}:{RPC_PASS}@{RPC_HOST}:{RPC_PORT}/{RPC_VHOST}'

broker_url = _url

result_backend = 'rpc://'

result_persistent = True

imports = ('rmxnmf.task', )

result_expires = 30
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

task_routes = {

    'rmxnmf.task.*': {'queue': 'rmxnmf'},

}

