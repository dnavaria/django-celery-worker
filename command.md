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
