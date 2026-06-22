from redis import Redis
from rq import Queue

conn_redis = Redis(
    host="localhost",
    port=6379
)

queue = Queue("pdf_queue", connection=conn_redis)