# -*- coding:utf-8 -*-
# Author:YEAR
li = [11, 22, 33, 44]
result = filter(lambda x: x > 22, li)
print(result)  # 具有生成指定条件数据能力的对象 在循环的时候才会生成


# 这就是python生成器, 使用函数创造

# 普通函数
def func():
    return 123


ret = func()


# 生成器 有yield
def func1():
    print('start')
    yield 1
    yield 2
    yield 3


# 当第一次循环进来会进入第一个yield拿走后面的东西 第二次循环会接着上次的位置向下执行到yield拿走后面的 以此类推
ret = func1()
print(ret)
for i in ret:
    print(i)

r = ret.__next__()  # 进入函数执行到yield,获取yield后面的数据退出 如果没有yield了就会报错
print(r)


# 基于生成器实现range功能
def myrange(arg):
    start = 0
    while True:
        if start > arg:
            return
        yield start
        start += 1


ret = myrange(10)
