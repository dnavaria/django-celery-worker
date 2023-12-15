import os

from celery import Celery
from kombu import Queue, Exchange
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")

app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# app.conf.task_routes = {
#     "cworker.tasks.task1": {"queue": "queue1"},
#     "cworker.tasks.task2": {"queue": "queue2"},
# }

# 5 tasks per minute
# app.conf.task_default_rate_limit = "5/m"

# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy": "priority",
# }

app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
]

# late ack after task is done
app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task
def add_numbers(x, y):
    return x + y

@app.task(queue='tasks')
def t1():
    time.sleep(2)
    return

@app.task(queue='tasks')
def t2():
    time.sleep(2)
    return

@app.task(queue='tasks')
def t3():
    time.sleep(2)
    return

app.autodiscover_tasks()
