# -*- coding:utf-8 -*-
# Author:YEAR
import threading
import time


# python中一个进程中只能用一个cpu,,,GIL全局解释器锁
# 进程:
#   优点:同时利用多个cpu,能够同时进行多个操作
#   缺点:耗费资源(重新开辟内存空间)
# 线程:
#   优点:共享内存,IO操作的时候,创造并发操作
#   缺点:抢占资源
# 进程不是越多越好,跟cpu个数一样最好
# 线程也不是越多越好,要具体分析,请求上下文十分耗时
# 进程和线程的目的是提高效率
# IO操作不利用cpu所以对于IO密集型用多线程计算密集型用多进程
# 单进程单线程,主进程主线程
# 自定义线程:主进程主线程子线程

# 线程基本
# def show(arg):
#     time.sleep(1)
#     print('thread:', arg)
#
#
# for i in range(10):
#     t = threading.Thread(target=show, args=(i,))
#     t.start()
#
# print('main thread stop')


class myThread(threading.Thread):
    def __init__(self, num):
        super(myThread, self).__init__()
        self.num = num

    def run(self):
        print('running on number:%s' % self.num)
        time.sleep(3)


# 线程锁
gl_num = 0

lock = threading.RLock()


def show(arg):
    lock.acquire()
    global gl_num
    time.sleep(1)
    gl_num += 1
    print(gl_num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

# 信号量
semaphore = threading.BoundedSemaphore(5)


def show1(arg):
    semaphore.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    semaphore.release()


for i in range(20):
    t = threading.Thread(target=show1, args=(1,))
    t.start()


# 事件
def show2(event):
    print('thread start')
    event.wait()
    print('thread execute')


event_obj = threading.Event()
for i in range(20):
    t = threading.Thread(target=show2, args=(event_obj,))
    t.start()

event_obj.clear()
inp = input('input:')
if inp == "start":
    event_obj.set()

# 条件

con = threading.Condition()


def show3(arg):
    con.acquire()
    con.wait()
    print('run the thread %s' % arg)
    con.release()


for i in range(20):
    t = threading.Thread(target=show3, args=(i,))
    t.start()

while True:
    inp = input('>>>')
    if inp == 'q':
        break
    else:
        con.acquire()
        con.notify(int(inp))
        con.release()


# 条件2
def condition_func():
    ret = False
    inp = input('>>>')
    if inp == '1':
        ret = True

    return ret


def show4(arg):
    con.acquire()
    con.wait_for(condition_func())
    print('run the thread %s' % arg)
    con.release()


# 定时器
def hello():
    print('Hello')


t = threading.Timer(1, hello)
t.start()

# 进程基本
from multiprocessing import Process


def p(arg):
    print('hello %s' % arg)


for i in range(10):
    p = Process(target=p, args=(i,))
    p.start()

# 进程各自持有一份数据,默认数据无法共享
li = []


def p1(arg):
    li.append(arg)
    print('say ', li)


for i in range(10):
    p = Process(target=p1, args=(1,))
    p.start()
print('ending', li)

# Array共享进程数据
from multiprocessing import Array

temp = Array('i', [11, 222, 333, 444])


def p2(arg):
    temp[arg] = 100 + arg
    for item in temp:
        print(arg, '------>', item)


for i in range(2):
    p = Process(target=p2, args=(i))
    p.start()

# dict()共享
from multiprocessing import Manager

manage = Manager()
dic = manage.dict()


def p3(arg):
    dic[arg] = 100 + arg
    print(dic.values())


for i in range(2):
    p = Process(target=p3, args=(1,))
    p.start()
    p.join()

# Queue共享
from multiprocessing import Queue


def p4(i, q):
    print(i, q.get())


q = Queue()
q.put("h1")
q.put("h2")
q.put("h3")
for i in range(2):
    p = Process(target=p4, args=(i, q,))
    p.start()

# 进程锁
from multiprocessing import RLock


def p5(lock, temp, i):
    lock.acquire()
    temp[0] = 100 + i
    for item in temp:
        print(i, '------>', item)
    lock.release()


lock = RLock()
temp = Array('i', [11, 22, 33, 44])
for i in range(20):
    p = Process(target=p5, args=(lock, temp, i,))
    p.start()

# 进程池
from multiprocessing import Pool


def p6(i):
    time.sleep(1)
    return i + 100


def p7(i):
    print(i)


pool = Pool(5)
for i in range(10):
    pool.apply_async(func=p6, args=(i,), callback=p7)
print('end')
pool.close()
pool.join()

# 协程
from greenlet import greenlet


def test1():
    print('12')
    gr2.switch()
    print('34')
    gr2.switch()


def test2():
    print('56')
    gr1.switch()
    print('78')


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()

import gevent


def foo():
    print('foo now')
    gevent.sleep(0)
    print('foo again')


def boo():
    print('boo now')
    gevent.sleep(0)
    print('boo now')


gevent.joinall([gevent.spawn(foo), gevent.spawn(boo)])
# if __name__ == '__main__':
#     t1 = myThread(1)
#     t2 = myThread(2)
#     t1.start()
#     t2.start()
