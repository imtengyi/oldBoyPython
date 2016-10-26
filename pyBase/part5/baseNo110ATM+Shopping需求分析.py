# -*- coding:utf-8 -*-
# Author:YEAR
# ATM+购物商城程序
# 角色 管理员,,普通用户的增删查改,,记录用户基本信息,,普通用户额度 普通用户,,提现收手续费,,多账户登录,,账户转账,,消费流水,,还款接口,,atm操作日志
# 程序目录结构 bin目录 config目录 db目录 lib目录 src目录


# 用户基本信息存储形式 db目录中有admin和userinfo目录 admin为管理员信息,,每个用户一个文件 userinfo为普通用户,,每个用户一个文件夹以银行卡号为名,,里面有record文件夹和基本信息文件
# 普通用户基本信息格式
base_info = {
    'username': 'year',
    'card': 123123123,
    'password': 8889,
    'credit': 15000,  # 行用卡额度
    'balance': 15000,  # 本月可用额度
    'saving': 0,  # 储蓄金额
    'enroll_date': '2016-01-01',
    'expire_date': '2021-01-01',
    'status': 0,  # 0=normal 1=locked 2=disable
    'debt': []  # 欠款记录
}
