import time
from celery import shared_task

@shared_task(task_rate_limit='5/m')
def task1(queue='celery'):
    time.sleep(2)
    return

@shared_task
def task2(queue='celery:1'):
    time.sleep(2)
    return

@shared_task
def task3(queue='celery:2'):
    time.sleep(2)
    return

@shared_task
def task4(queue='celery:3'):
    time.sleep(2)
    return