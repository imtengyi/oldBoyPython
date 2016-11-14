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
WELCOMESTRING = '{hello:*^40s}'.format(hello='ATM机')
ERROR_CARD = {'cardno': '', 'errorno': 0}


def getUserInfo(cardno):
    """
    取得用户的信息
    :param cardno:用户卡号
    :return: 用户的账户信息字典对象
    """
    userDic = {}
    userinfopath = os.path.join(os.path.join(USERDB, cardno), 'user_info')
    if os.path.exists(userinfopath):
        userDic = json.load(open(userinfopath, 'r'))
        return userDic
    else:
        return userDic


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
        # cmdColor.print_okgreen('修改成功!!')
    except:
        cmdColor.print_fail('修改失败!!')


def run():
    """
    运行ATM程序的入口
    :return:
    """
    while True:
        cmdColor.print_header(WELCOMESTRING)
        if not LOGGIN_USER['logginFlag']:
            cardno = input('Pls input your card number:')
            password = input('Pls input your password:')
            if os.path.exists(os.path.join(USERDB, cardno)):
                userInfo = getUserInfo(cardno)
                if userInfo:
                    if password == userInfo['password']:
                        if userInfo['status'] == 1:
                            cmdColor.print_fail('该卡已经被锁定,请联系管理员解锁!!')
                            continue
                        else:
                            LOGGIN_USER['logginFlag'] = True
                            LOGGIN_USER['userName'] = cardno
                            cmdColor.print_okgreen('Welcome %s' % (userInfo['username']))
                        continue
                    else:
                        if ERROR_CARD['cardno'] == cardno:
                            ERROR_CARD['errorno'] += 1
                            if ERROR_CARD['errorno'] == 3:
                                userInfo['status'] = 1
                                changeUserInfo(cardno, 'status', 1)
                                cmdColor.print_fail('该卡已经被锁定!!')
                        else:
                            ERROR_CARD['cardno'] = cardno
                            ERROR_CARD['errorno'] = 1
                            cmdColor.print_fail('连续输入错三次密码将锁定该卡')
                        continue
                else:
                    cmdColor.print_fail('卡号或密码错误请重新尝试!!')
                    continue
            else:
                cmdColor.print_fail('卡号或密码错误请重新尝试!!')
                continue
        else:
            userinfo = getUserInfo(LOGGIN_USER['userName'])
            choose_str = """
                1.查看基本信息
                2.存钱
                3.取钱
                4.还钱
                5.查看账单
                6.注销用户
                0.退出
                """
            print(choose_str)
            choose = input('>>>')
            if choose == '1':
                print('%-10s : %s' % ('额度', userinfo['credit']))
                print('%-10s : %s' % ('可用额度', userinfo['balance']))
                print('%-10s : %s' % ('余额', userinfo['saving']))
            elif choose == '2':
                savemoney = input('输入你想存入的金额:')
                if savemoney.isdigit():
                    changeUserInfo(LOGGIN_USER['userName'], 'saving', userinfo['saving'] + int(savemoney))
                    userinfo = getUserInfo(LOGGIN_USER['userName'])
                    cmdColor.print_okgreen('存入OK')
                    cmdColor.print_okgreen('当前余额是%d' % userinfo['saving'])
                else:
                    cmdColor.print_fail('输入错误!!')
            elif choose == '3':
                getmoney = input('输入你想提出的金额:')
                if getmoney.isdigit():
                    getmoney = int(getmoney)
                    if getmoney > userinfo['saving']:
                        cmdColor.print_fail('余额不足,最多只能提取 %d 元' % userinfo['saving'])
                    else:
                        changeUserInfo(LOGGIN_USER['userName'], 'saving', userinfo['saving'] - getmoney)
                        userinfo = getUserInfo(LOGGIN_USER['userName'])
                        cmdColor.print_okgreen('提款成功!!当前余额为 %d 元' % userinfo['saving'])
                else:
                    cmdColor.print_fail('输入错误!!!')
            elif choose == '4':
                pass
            elif choose == '5':
                pass
            elif choose == '6':
                LOGGIN_USER['logginFlag'] = False
                continue
            elif choose == '0':
                print('Goodbye!!')
                break
            else:
                continue


if __name__ == '__main__':
    cmdColor.print_header(WELCOMESTRING)
    # baba = getUserInfo('7274')
    # for key, value in baba.items():
    #     print('%s : %s' % (key, value))
    run()
