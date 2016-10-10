# -*- coding:utf-8 -*-
# Author:YEAR
# 打开文件
f1 = open('db', 'r', encoding='utf-8')  # 只读 encoding参数告诉python转化编码
data = f1.read()
print(data, type(data))  # 读出的为字符串类型,python默认做了编码转换将字节转换成了字符串,,
f1.close()
f1 = open('db', 'rb', encoding='utf-8')  # b表示2进制打开不要python做编码转换,写也一样
data = f1.read()
print(data, type(data))  # 读出的类型为字节类型
f1.close()

f2 = open('db', 'w')  # 只写 先清空源文件
f3 = open('db', 'x')  # 如果文件存在报错,,不存在创建并写内容
f5 = open('db', 'a')  # 追加
# +号 文件以可读可写打开
f1 = open('db', 'r+',
          encoding='utf-8')  # 文件位置指针 打开时在最开始 读完后 指针在最后,,再去写的时候会写在最后 python只要你读指针必会变到最后!! 所以写一般用r+不用a+ 也不用w+ w会清空

data = f1.read()  # read会按模式去读!!!
print(data, type(data))
f1.seek(1)  # seek会强行调整文件位置指针位置, 在其中某个位置写会覆盖其后的内容!!!! 永远是按字节方式找位置
f1.read(1)
f1.tell()  # 获取当前文件指针位置
f1.seek(f1.tell())  # 调整指针到指定位置
f1.write('888')
f1.close()

# 操作文件
f2.read()  # 无参数读全部 如果有参数 b按字节无b按字符
f2.tell()  # 获取当前指针位置
f2.seek(1)  # 跳转指针位置 永远按字节
f2.write('ss')  # 打开方式有关 有b只能写字节 无b写字符串
f2.fileno()  # 文件的数字形式描述符
f2.flush()  # 强刷 将写的内容强制刷新到硬盘上 close()会自动刷新
f2.isatty()  # 是否是tty设备
f2.readable()  # 是否可读
f2.seekable()  # 是否可移动指针
f2.readline()  # 只读一行
f2.truncate()  # 从文件指针位置截断数据 后面的删除

for line in f2:  # 迭代文件 一行一行
    pass
# 关闭文件
f1.close()
with open('db', 'a') as f4:
    pass
with open('db', 'a') as f6, open('db2', 'a') as f7:
    for line1 in f6:
        new_str = line1.replace('alex', 'st')
        f7.write(new_str)
    pass
