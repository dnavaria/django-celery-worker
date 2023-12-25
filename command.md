# Commands


## Task Grouping

```python-repl
from celery import group
from cworker.tasks import task1,task2,task3,task4
task_group = group(task1.s(),task2.s(),task3.s(),task4.s())
task_group.apply_async()
```


## Task Chaining

```python-repl
from celery import chain
from cworker.tasks import task1,task2,task3,task4
task_chain = chain(task1.s(),task2.s(),task3.s(),task4.s())
task_chain.apply_async()
```


## RabbitMQ Tasks

```python
from dcelery.celery import t1,t2,t3
t1.apply_async(priority=5, queue="tasks")
t2.apply_async(priority=6, queue="tasks")
t3.apply_async(priority=7, queue="tasks")
t2.apply_async(priority=8, queue="tasks")
t1.apply_async(priority=9, queue="tasks")
t3.apply_async(priority=10, queue="tasks")
```

## Tasks with args and keyword arguments
    
```python
from dcelery.celery import t1
t1.apply_async(args=[2,3], kwargs={"message": "The Sum is:"})
```

### Celery Inspect Commands
```bash
celery inspect active_queues
celery inspect active
```