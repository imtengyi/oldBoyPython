# -*- coding:utf-8 -*-
# Author:YEAR



# 双层装饰器 原理弄清楚
USER_INFO = {}


def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print('请登录')

    return inner


def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("无权查看")

    return inner


@check_login
@check_admin
def index():
    """
    管理员才能看
    :return:
    """
    pass


def home():
    pass


def login():
    user = input('输入用户名')
    if user == 'admin':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True


def main():
    inp = input('1.login;2.info;3.admin')
    if inp == '1':
        login()
    elif inp == '2':
        home()
    elif inp == '3':
        index()
