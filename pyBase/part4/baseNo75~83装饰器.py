# -*- coding:utf-8 -*-
# Author:YEAR
# 对象封闭原则 利用装饰器来实现添加功能而不修改本身
# @+函数名 自动执行outer函数并且将下面的函数名f1当做参数传递给outer  将outer函数的返回值重新赋值给f1
# 注意内置函数的参数
def outer(func):
    def inner(a):
        print('log')
        ret = func(a)
        print('after')
        return ret

    return inner


def outer1(func):
    def inner(*args, **kwargs):
        print('log')
        ret = func(*args, **kwargs)
        print('after')
        return ret

    return inner


@outer
def f1(a):
    print('f1')


# 装饰器最常用的功能 权限的管理
LOGIN_USER = {"is_login": False}


def outer2(func):
    def inner(*args, **kwargs):
        if LOGIN_USER["is_login"]:
            r = func()
            return r
        else:
            print("请登录")

    return inner


@outer2
def changepwd():
    pass


@outer2
def manager():
    print("欢迎%s登录" % LOGIN_USER["current_user"])


def login(user, pwd):
    if user == 'alex' and pwd == '123':
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = user


def main():
    inp = input("1.后台管理;2.登录")
    if inp == '1':
        manager()
    elif inp == '2':
        username = input("请输入用户名")
        pwd = input('请输入密码')
        login(username, pwd)
