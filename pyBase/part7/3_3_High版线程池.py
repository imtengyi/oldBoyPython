# -*- coding:utf-8 -*-
# Author:YEAR
import queue
import threading
import contextlib
import time

StopEvent = object()


class THreadPool(object):
    def __init__(self, max_num):
        self.q = queue.Queue()
        # 最多创建的线程数(线程池最大容量)
        self.max_num = max_num

        self.terminal = False
        # 真实创建的线程列表
        self.generate_list = []
        # 空闲线程数量
        self.free_list = []

    def run(self, func, args, callback=None):
        w = (func, args, callback,)
        self.q.put(w)

        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()

    def generate_thread(self):
        """
        创建一个新线程
        :return:
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        :return:
        """
        # 获取当前线程
        current_thread = threading.currentThread
        self.generate_list.append(current_thread)

        # 取任务并执行
        event = self.q.get()
        while event != StopEvent:
            # 是元组 是任务
            # 解开任务包
            # 执行任务
            func, args, callback = event
            status = True
            try:
                ret = func(*args)
            except Exception as e:
                status = False
                ret = e
            if callback != None:
                try:
                    callback(status, ret)
                except Exception as e:
                    pass
            # 标记我空闲了
            # 取任务包
            # 标记我不空闲
            if not self.terminal:
                # 这里可以用上下文管理实现
                self.free_list.append(current_thread)
                event = self.q.get()
                self.free_list.remove(current_thread)
            else:
                event = StopEvent
        else:
            # 不是元组 不是任务 任务结束
            self.generate_list.remove(current_thread)

    def close(self):
        num = len(self.generate_list)
        while num:
            self.q.put(StopEvent)
            num -= 1

    def terminate(self):
        self.terminal = True
        num = len(self.generate_list)
        self.q.empty()
        while num:
            self.q.put(StopEvent)
            num -= 1


def work(i):
    print(i)


pool = THreadPool(10)
for i in range(50):
    # 将任务放在队列中
    # 着手开始处理任务
    #   -创建线程
    #       -有空闲线程,则不再创建线程
    #       -没有空闲线程,创建线程,前提是不能高于线程池的限制,根据任务个数判断
    #   -线程去队列中取任务
    pool.run(func=work, args=(i,))

pool.close()
