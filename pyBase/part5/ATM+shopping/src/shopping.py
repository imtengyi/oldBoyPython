# -*- coding:utf-8 -*-
# Author:YEAR
import os
import json
import sys
import datetime
import shutil
import datetime

LIBDIC = os.path.join(os.path.dirname(os.getcwd()), 'lib')
sys.path.append(LIBDIC)
import cmdColor

LOGGIN_USER = {'logginFlag': False, 'userName': ''}
USERDB = os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'db'), 'user')
WELCOMESTRING = '{hello:*^40s}'.format(hello='大利佳超市')
DALIJIA = {'1': ['cpu', 3000], '2': ['主板', 4000], '3': ['显卡', 5000], '4': ['风扇', 99], '5': ['机箱', 1000]}
SHOPPINGCAR = {}


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


def getShoppingcarStr(shoppingcar):
    loggingStr = ''
    needMoney = 0
    if shoppingcar:
        loggingStr = '|' + '商品名称'.center(16) + '|' + '单价'.center(10) + '|' + '数量'.center(10) + '|' + '应付价格'.center(
            10) + '\n'
        for id, count in SHOPPINGCAR.items():
            loggingStr += (
                '|' + DALIJIA[id][0].center(16) + '|' + str(DALIJIA[id][1]).center(10) + '|' + str(count).center(
                    10) + '|' + str(
                    count * DALIJIA[id][1]).center(10) + '\n')
            needMoney += count * DALIJIA[id][1]
        loggingStr += '共计:%s元\n' % str(needMoney)
        return loggingStr, needMoney
    else:
        return loggingStr, needMoney


def run():
    """
    shopping程序的入口
    :return:
    """
    while True:
        cmdColor.print_header(WELCOMESTRING)
        if not LOGGIN_USER['logginFlag']:
            cardno = input('Pls input your card number:')
            password = input('Pls input your password:')
            if os.path.exists(os.path.join(USERDB, cardno)):
                userinfo = getUserInfo(cardno)
                if userinfo:
                    if password == userinfo['password']:
                        LOGGIN_USER['logginFlag'] = True
                        LOGGIN_USER['userName'] = cardno
                        cmdColor.print_okgreen('Welcome %s !!' % userinfo['username'])
                    else:
                        cmdColor.print_fail('用户名密码错误!!')
                else:
                    cmdColor.print_fail('用户名密码错误!!')
            else:
                cmdColor.print_fail('用户名密码错误!!')
        else:
            userinfo = getUserInfo(LOGGIN_USER['userName'])
            cmdColor.print_header('Choose what you want %s' % userinfo['username'])
            choose_str = """
                1.cpu    :  3000元
                2.主板    :  4000元
                3.显卡    :  5000元
                4.风扇    :  99元
                5.机箱    :  1000元
                0.注销用户!!
                g.查看购物车!!!
                q.退出系统!!
            """
            print(choose_str)
            choose = input('>>>')
            if choose == '1':
                if SHOPPINGCAR.get('1'):
                    SHOPPINGCAR['1'] += 1
                else:
                    SHOPPINGCAR['1'] = 1
            elif choose == '2':
                if SHOPPINGCAR.get('2'):
                    SHOPPINGCAR['2'] += 1
                else:
                    SHOPPINGCAR['2'] = 1
            elif choose == '3':
                if SHOPPINGCAR.get('3'):
                    SHOPPINGCAR['3'] += 1
                else:
                    SHOPPINGCAR['3'] = 1
            elif choose == '4':
                if SHOPPINGCAR.get('4'):
                    SHOPPINGCAR['4'] += 1
                else:
                    SHOPPINGCAR['4'] = 1
            elif choose == '5':
                if SHOPPINGCAR.get('5'):
                    SHOPPINGCAR['5'] += 1
                else:
                    SHOPPINGCAR['5'] = 1
            elif choose == '0':
                LOGGIN_USER['logginFlag'] = False
                continue
            elif choose == 'g':
                loggingStr, needMoney = getShoppingcarStr(SHOPPINGCAR)
                if loggingStr:
                    print(loggingStr)
                    shoppingStr = """
                        1.结算
                        2.继续购物
                    """
                    while True:
                        print(shoppingStr)
                        usercmd = input('>>>')
                        if usercmd == '1':
                            if (userinfo['balance'] >= needMoney):
                                loggingStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n' + loggingStr
                                if os.path.exists(
                                        os.path.join(os.path.join(USERDB, LOGGIN_USER['userName']), 'shoppingLog')):
                                    with open(
                                            os.path.join(os.path.join(USERDB, LOGGIN_USER['userName']), 'shoppingLog'),
                                            'a') as flog:
                                        flog.write(loggingStr)
                                else:
                                    with open(
                                            os.path.join(os.path.join(USERDB, LOGGIN_USER['userName']), 'shoppingLog'),
                                            'w') as flog:
                                        flog.write(loggingStr)
                                newbalance = userinfo['balance'] - needMoney
                                newdebt = userinfo['debt']
                                if newdebt.get(datetime.datetime.now().strftime("%Y-%m")):
                                    newdebt[datetime.datetime.now().strftime("%Y-%m")] += needMoney
                                else:
                                    newdebt[datetime.datetime.now().strftime("%Y-%m")] = needMoney
                                changeUserInfo(LOGGIN_USER['userName'], 'balance', newbalance)
                                changeUserInfo(LOGGIN_USER['userName'], 'debt', newdebt)
                                userinfo = getUserInfo(LOGGIN_USER['userName'])
                            else:
                                print('你的额度不够买尼玛!!')
                                continue
                        elif usercmd == '2':
                            break
                        else:
                            continue
                else:
                    print('你的购物车没有任何东西,去选购吧!')
                    input('任意键继续...')
            elif choose == 'q':
                print('GoodBye!!')
                break
            else:
                continue


if __name__ == '__main__':
    cmdColor.print_header(WELCOMESTRING)
    run()
