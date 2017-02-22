# -*- coding:utf-8 -*-
# Author:YEAR
import queue
import threading


class ThreadPool(object):
    def __init__(self, max_num):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def func(pool, a):
    print(a)
    pool.add_thread()


p = ThreadPool(20)

for i in range(100):
    thread = p.get_thread()
    t = thread(target=func, args=(p, i,))
    t.start()
