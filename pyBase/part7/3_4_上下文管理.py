# -*- coding:utf-8 -*-
# Author:YEAR
import queue

q = queue.Queue()
li = []

li.append(1)
q.get()
li.remove(1)

import contextlib

@contextlib.contextmanager
def worker_state(xxx,val):
    xxx.append(val)
    try:
        yield
    finally:
        xxx.remove(val)

with worker_state(li,1):
    q.get()