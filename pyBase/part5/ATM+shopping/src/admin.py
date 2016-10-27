# -*- coding:utf-8 -*-
# Author:YEAR
import os
import json
import sys

LIBDIC = os.path.join(os.path.dirname(os.getcwd()), 'lib')
sys.path.append(LIBDIC)
import cmdColor

LOGGIN_USER = {'logginFlag': False, 'userName': ''}
ADMINDB = os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'db'), 'admin')
WELCOMESTRING = '{hello:*^40s}'.format(hello='后台管理')


def createAdmin():
    """
    创建一个admin用户,将admin用户信息序列化到db下的admin文件夹
    :return: True创建成功 False创建失败
    """
    admin_info = {'adminName': 'year', 'password': 'year93926'}
    try:
        json.dump(admin_info, open(os.path.join(ADMINDB, 'year'), 'w'))
    except:
        print('Create Field!!')
        return False
    return True


def getAdminInfo(name):
    """
    根据参数name去找到相应的管理员信息
    :param name:用户名
    :return: 空字典:获取失败 admindic:获取成功 返回admin信息字典
    """
    adminDic = {}
    if os.path.exists(os.path.join(ADMINDB, name)):
        adminDic = json.load(open(os.path.join(ADMINDB, name), 'r'))
        return adminDic
    else:
        return adminDic


def run():
    """
    运行atm管理后台程序的入口函数 主流程
    :return:
    """

    pass


if __name__ == '__main__':
    print(ADMINDB)
    print(cmdColor.Logger.HEADER + WELCOMESTRING + cmdColor.Logger.ENDC)
    # createAdmin()
    # adminDic = getAdminInfo('year')
    # if adminDic:
    #     print(adminDic['adminName'], adminDic['password'])
    # else:
    #     print('给你一个飞天大草')
