# -*- coding:utf-8 -*-
# Author:YEAR
# python正则表达式
# 正则表达式本来就是一门小小的变成语言 python使用的是re提供的接口 所以第一步要导入re模块
import re

# findall 将匹配的所有字符串以列表的方式返回 第一个参数是规则 第二个参数是被寻找的对象
re.findall('year', 'asdfasdfsdferyearasdfeg')
# 字符匹配 分为普通字符和元字符
# 元字符: . ^ $ * + ? {} [] | () \ 每个都有自己的特殊意义
# .除换行符以外的任何一个字符
re.findall('y.ar', 'asdfasdfsdferyearasdfeg')
re.findall('y.ar', 'asdfasdfsdfery\narasdfeg')
# ^在起始位置匹配
re.findall('^y.ar', 'yearasdfasdfsdferyearasdfeg')
re.findall('^y.ar', 'asdfasdfsdferyearasdfeg')
# $在结束位置匹配
re.findall('y.ar$', 'asdfasdfsdferyearasdfegyear')
# * + ? {} 重复
# *匹配0到多个
re.findall('y.*ar$', 'asdfasdfsdferyearasdfegyear')
# +匹配1到多次
re.findall('y.+ar$', 'asdfasdfsdferyearasdfegyear')
# ?50到1次
re.findall('y.?ar$', 'asdfasdfsdferyearasdfegyear')
# {}指定重复次数
re.findall('y.{1,5}ar$', 'asdfasdfsdferyearasdfegyear')
re.findall('y.{,5}ar$', 'asdfasdfsdferyearasdfegyear')  # 从零开始
# []指定匹配字符集内的字符 或的作用 []内的字符里 元字符没有特殊意义 除了 -表示范围 ^非的意思 \转译 \d数字
re.findall('y[abce]{,5}ar$', 'asdfasdfsdferyearasdfegyear')
re.findall('y[a-z]{,5}ar$', 'asdfasdfsdferyearasdfegyear')
# \加元字符是取消元字符的意义 \跟普通字符形成特殊意义的元字符
# \d任意十进制数字[0-9] \D任意非数字字符 \s任何空白字符 \S任何非空白字符 \w任何字母数字字符下划线 \W任何非字母数字字符下划线 \b匹配一个单词边界(\w和\W间的) 单词指连续的字母数字下划线组成的
re.findall('I', 'I am handIsome')
re.findall(r'I\b', 'I am handIsome')
re.findall(r'I\b', 'I%am handIsome')
