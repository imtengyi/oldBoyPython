# -*- coding:utf-8 -*-
# Author:YEAR


def login(user, pwd):
    """
    用于用户登录
    :param user: 用户输入的用户名
    :param pwd: 用户输入的密码
    :return: true表示成功 False表示失败
    """
    f = open("db", 'r')
    for line in f:
        line_list = line.strip().split("|")
        if line_list[0] == user and line_list[1] == pwd:
            return True
    return False


def register(user, pwd):
    """
    用于用户注册
    :param user: 用户名
    :param pwd: 密码
    :return: True注册成功
    """
    f = open("db", 'a')
    temp = user + "|" + pwd
    f.write(temp)
    return True


def main():
    t = input("1:登录;2:注册")
    if t == '1':
        user = input("请输入用户名")
        pwd = input("请输出密码")
        r = login(user, pwd)
        if r:
            print("登录成功")
        else:
            print("登录失败")
    else:
        user = input("请输入用户名")
        pwd = input("请输出密码")
        r = register(user, pwd)


main()
