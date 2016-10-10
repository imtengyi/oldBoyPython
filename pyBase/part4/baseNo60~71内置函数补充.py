# -*- coding:utf-8 -*-
# Author:YEAR


def f1():
    pass


callable(f1)  # 检测对象是否可以被执行

print(chr(65))  # ascii码转换成字符
print(ord('a'))  # ascci码转换成二进制

import random

i = random.randrange(1, 5)  # 在范围内产生随机数 1=<i<5
print(i)
# 生成随机验证码
li = []
for i in range(6):
    r = random.randrange(0, 5)
    if r == 2 or r == 4:
        num = random.randrange(0, 10)
        li.append(str(num))
    else:
        temp = random.randrange(65, 91)  # 利用产生随机数 由ascii码将数字转换成字符从而达到随机字符的效果
        c = chr(temp)
        li.append(c)
''.join(li)  # 将随机字符列表变成随机字符串

r = compile('print(123)', '<string>',
            'exec')  # 编译字符串得到一个codeobject 三种模式 single(编译成单行程序) eval(编译成表达式) exec(编译成python一模一样的东西)
exec(r)  # 执行一个code object或者字符串 没有返回值

eval('')  # 把字符串当成一个表达式 执行并返回结果

# 反射delattr getattr setattr

# dict()字典

# dir()快速查看 一个类的功能方法
dir(dict)
help(dict)  # 告诉你一个类的使用手册

# 共97页,每页显示10页需要多少页 divmod
r = divmod(97, 10)  # 返回元组 r[0]为商 r[1]为余数
n1, n2 = r

isinstance(r, tuple)  # 判断对象是否是指定类的实例


# filter函数 接收一个函数和可迭代对象 循环可迭代对象 调用指定函数 返回True将迭代对象加入最后列表 和lamnda一起用 high
def f3(a):
    if a > 22:
        return True


f4 = lambda a: a > 30
li = [11, 22, 33, 44]
ret = filter(f3, li)
print(list(ret))

# map 接收一份函数和可迭代对象 循环可迭代对象调用指定函数进行处理 加入最后返回 和lamnda一起用 high
f5 = lambda a: a + 100
biubiubiu = map(f5, li)

# 获取所有的全局变量和局部变量 globals() locals()

# 生成哈希值 hash() 例如字典会先将key转换成hash值然后去存储
s = 'asdfasdfasdfasdfasdf'
print(hash(s))

# 最大最小 max() min()

# memoryview() 查看内存地址

pow(2, 10)  # 求幂

repr(s)  # 调用类里面的__repr__方法
reversed(s)  # 调用类里面的__reversed__方法
round(1.8)  # 四舍五入
# slice 切片
sorted(li)  # 排序 同li.sort()
l1 = ['111', 222, 3333]
l2 = ['222', 222, 3333]
r = zip(l1, l2)  # 混合 将每个元素的相同位置元素组成元组放入结果中, 如果有混合的两个元素中有长短则舍弃长的部分
