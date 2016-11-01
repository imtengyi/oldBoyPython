# -*- coding:utf-8 -*-
# Author:YEAR
import os
import json
import sys
import datetime
import shutil

LIBDIC = os.path.join(os.path.dirname(os.getcwd()), 'lib')
sys.path.append(LIBDIC)
import cmdColor

LOGGIN_USER = {'logginFlag': False, 'userName': ''}
ADMINDB = os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'db'), 'admin')
USERDB = os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'db'), 'user')
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


def creatUser(card, username, password, credit):
    """

    :param username: 用户名
    :param password: 用户密码
    :param credit: 用户信用卡额度
    :return: True:成功
    :return: False:失败
    """
    try:
        userdir = os.path.join(USERDB, card)
        os.mkdir(userdir)
        base_info = {
            'username': username,
            'card': card,
            'password': password,
            'credit': credit,  # 行用卡额度
            'balance': credit,  # 本月可用额度
            'saving': 0,  # 储蓄金额
            'enroll_date': datetime.date.today().strftime("%Y-%m-%d"),
            'expire_date': (datetime.date.today() + datetime.timedelta(days=3650)).strftime("%Y-%m-%d"),
            'status': 0,  # 0=normal 1=locked 2=disable
            'debt': []  # 欠款记录
        }
        json.dump(base_info, open(os.path.join(userdir, 'user_info'), 'w'))
        return True
    except:
        return False


def changeUserInfo(witchuser, witchinfo, changewhat):
    """

    :param witchinfo:需要修改哪个信息
    :param changewhat: 需要修改成什么
    :return:
    """
    try:
        userinfodir = os.path.join(USERDB, witchuser)
        userDic = json.load(open(os.path.join(userinfodir, 'user_info'), 'r'))
        userDic[witchinfo] = changewhat
        json.dump(userDic, open(os.path.join(userinfodir, 'user_info'), 'w'))
        cmdColor.print_okgreen('修改成功!!')
    except:
        cmdColor.print_fail('修改失败!!')


def run():
    """
    运行atm管理后台程序的入口函数 主流程
    :return:
    """
    while True:
        cmdColor.print_header(WELCOMESTRING)
        if not LOGGIN_USER['logginFlag']:
            adminname = input("Admin name:")
            password = input("password:")
            if os.path.exists(os.path.join(ADMINDB, adminname)):
                admin_dic = getAdminInfo('year')
                if admin_dic:
                    if adminname == admin_dic['adminName'] and password == admin_dic['password']:
                        LOGGIN_USER['logginFlag'] = True
                        LOGGIN_USER['userName'] = adminname
                        cmdColor.print_okgreen('Welcome %s' % (adminname))
                        continue
                    else:
                        cmdColor.print_fail('用户名或密码错误请重新尝试!!')
                        continue
                else:
                    cmdColor.print_fail('用户名或密码错误请重新尝试!!')
                    continue
            else:
                cmdColor.print_fail('用户名或密码错误请重新尝试!!')
                continue
        else:
            choose_str = """
            1.创建用户
            2.删除用户
            3.修改用户信息
            4.注销用户
            0.退出
            """
            print(choose_str)
            choose = input('>>')
            if choose == '1':
                card = input('创建的卡号:')
                if not os.path.exists(os.path.join(USERDB, card)):
                    username = input('创建的用户名:')
                    pwd = input('创建用户密码:')
                    credit = input('创建用户额度')
                    if creatUser(card, username, pwd, credit):
                        cmdColor.print_okgreen('创建成功!!')
                    else:
                        cmdColor.print_fail('创建失败!!')
                else:
                    cmdColor.print_fail('卡号已经存在')
            elif choose == '2':
                card = input('您需要删除的账号名:')
                if not os.path.exists(os.path.join(USERDB, card)):
                    print('根本没有这个用户!!')
                else:
                    try:
                        shutil.rmtree(os.path.join(USERDB, card))
                        continue
                    except:
                        print('删除失败!!')
                        continue
            elif choose == '3':
                print('{hello:-^40s}'.format(hello='目前只可更改账户可用额度!'))
                userneedtochange = input('你需要修改哪个用户:')
                if not os.path.exists(os.path.join(USERDB, userneedtochange)):
                    print('根本没有这个用户!!')
                else:
                    changewhat = int(input('输入需要修改的额度'))
                    changeUserInfo(userneedtochange, 'credit', changewhat)

            elif choose == '4':
                LOGGIN_USER['logginFlag'] = False
                continue
            elif choose == '0':
                break
            else:
                continue


if __name__ == '__main__':
    # print(ADMINDB)
    cmdColor.print_header(WELCOMESTRING)
    cmdColor.print_okblue(WELCOMESTRING)
    cmdColor.print_okgreen(WELCOMESTRING)
    cmdColor.print_warning(WELCOMESTRING)
    cmdColor.print_fail(WELCOMESTRING)

    run()
    # print(cmdColor.Logger.HEADER + WELCOMESTRING + cmdColor.Logger.ENDC)
    # createAdmin()
    # adminDic = getAdminInfo('year')
    # if adminDic:
    #     print(adminDic['adminName'], adminDic['password'])
    # else:
    #     print('给你一个飞天大草')
