from dotenv import load_dotenv
load_dotenv()
from rq import SimpleWorker
from client.rq_client import conn_redis

worker = SimpleWorker(["query_queue"], connection=conn_redis)

worker.work()