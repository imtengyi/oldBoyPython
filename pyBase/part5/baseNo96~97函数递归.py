# -*- coding:utf-8 -*-
# Author:YEAR
# python递归
def a():
    return '123'


def b():
    r = a()
    return r


def c():
    r = b()
    print(r)


def func(n):
    n += 1
    if n >= 10:
        return 'end'
    return func(n)


def func1(arg):
    if arg <= 1:
        return 1
    return arg * func1(arg - 1)
