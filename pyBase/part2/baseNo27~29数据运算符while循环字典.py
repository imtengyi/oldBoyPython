# -*- coding:utf-8 -*-
# Author:YEAR
# 1.1数据运算 加减乘除不说 %号为取余数,,常用来判断奇偶数 **幂运算 //取整除,,返回商的整数部分
print(8 % 2)
print(10 // 3)
# 1.2运算符 == != <> < > >= <=没什么好说的
# 1.3赋值运算 = += -= *= /= %= **= //= 同样没什么好说的
# 1.4逻辑运算 and or not 更没有什么好说的了
# 1.5成员运算 in ,, not in 同样没什么好说的
# 1.6身份运算 is ,, is not 判断两个标识符是不是引用自一个对象
a = [1, 2, 3, 4]
print(type(a) is list)
# 1.7位运算 & | ^异或 ~取反 << >> 二进制知识 计算机中能表示的最小单位和能存储的最小单位就是一个二进制位(bit) 8bit=byte(字节) 1024byte=1kbyte等等
a = 60  # 00111100
b = 13  # 00001101
c = 0

c = a & b  # 12=00001100
c = a | b  # 61=00111101
c = a ^ b  # 49=00110001 相同为0不同为1
c = ~a  # 195=11000011 按位取反 结果为195-256
print(64 >> 1)  # 右移1位就是除2 右移2位就是除2再除2
print(64 << 1)  # 左移1位就是乘以2 位移动比直接用乘除运算快

# 1.8运算级 有一些细节的运算级 大体上没什么好说的

# 2.1while循环 while True: 少写死循环
count = 0
while True:
    if count > 50 and count < 60:
        print("hahahahah")
        count += 1
        continue
    count += 1
    if count == 100:
        print("100")
        break
oke = 0

# 3.1字典 {}键值对 天然去重 字典是无序的
id_db = {
    123123123: {
        'jjj': 'asdf',
        'asdf': 'fdfdf'
    }
}
print(id_db[123123123])
# 3.2字典操作 添加,,直接写key=value 删除,,del .pop() 拷贝,,参考列表拷贝 取值一般用get()防报错 更新字典dic1.update(dic2),,存在相应的key就更新相应的值,不存在就会添加  转换为列表(键值对转换为元组，，元组组成列表)dic.items()一般不用  取所有value和key,,dic.values().keys()
id_db[124124124] = 'asdfasdf'
del id_db[124124124]
id_db[123123123].pop('jjj')
id1 = id_db.get(123123123)
id_db2 = {
    123123123: {
        'asdf': 'biubiubiu'
    },
    'hahaha': 'enenene'
}
id_db.update(id_db2)
id_db.items()
id_db.values()
id_db.keys()

# 3.3字典操作2 判断字典有没有key,,用key in dic  加入空值键dic.setdefault(key,value),,如果存在该键就返回值否则就生成空值键,,也可以指定value 加入多个相同value的key,,dic.fromkeys([1,2,3,4,5],'ddddd')但是这是类方法和对象本身没有关系！！
print(123123123 in id_db)
id_db.setdefault(125125125, 'hahaha')
id_db.fromkeys([1, 2, 3, 4, 5, 6], 'sssss')

# 3.4字典操作3 随机删除dic.popitem()不要用 字典循环1 for key,value in dic.items()不好,,有一个dic到list的转换过程 循环2 for key in dic:
id_db.popitem()
for key in id_db:
    print(id_db[key])
