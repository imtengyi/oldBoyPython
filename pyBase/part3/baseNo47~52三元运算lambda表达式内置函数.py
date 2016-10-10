# -*- coding:utf-8 -*-
# Author:YEAR


# 1.1三元运算,三目运算 简单的ifelse可以用此方式
name = 'year' if 1 == 1 else 'SB'
# 1.2lambada表达式 简单的function可以用此方式
f2 = lambda a1: a1 + 100
# 2.1内置函数
# abs()绝对值
n = abs(-1)
# all() any()  0,None 负数 空字符串 空列表 空字典 空元组是false
# all接收一个可迭代的对象 有一个是假就是假 所有为真才是真 any为任何一个为真就是真
n = all([11, 22, 33, 44, ''])
n = any([11, 22, 33, 44, 55])


# ascii() #自动执行对象的__repr__方法
class Foo:
    def __repr__(self):
        return "111"


n = ascii(Foo())

# bin() oct() hex() 分别接收十进制转换成2进制8进制16进制
print(bin(5))
print(oct(7))
print(hex(9))
# utf-8编码一个汉字三个字节 gbk一个汉字两个字节
# 字符串转换成字节类型 用bytes()
print(bytes('周', encoding='utf-8'))
# 字节转换成字符串 用str
print(str(bytes('周', encoding='utf-8'), encoding='utf-8'))
