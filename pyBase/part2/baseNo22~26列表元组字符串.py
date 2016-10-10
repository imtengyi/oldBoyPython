# -*- coding:utf-8 -*-
# Author:YEAR
import copy

# import baseNo22Sub
# pyc python是一个先编译后解释的语言 pyc是pythoncodeobject的持久化保存
# 格式化字符串，，如果用加号拼接字符串会在内存中开辟多块空间 在使用时会进行多次搜寻，不好。。

# 1.1列表..其他语言叫数组，python牛逼
age = 23
name = ["biubiubiu", "jiujiujiu", 22, age]
# namecopy = name
# namecopy.pop()
print(name)
# print(namecopy)
# 1.2列表取值 正常index 从零开始，，取倒数加负号 倒数第一就是[-1]
# 1.3列表切片 [0:2]取得是第一个和第二个，，也就是头取尾不取  取值永远按照列表顺序例如取倒数[-5:-1]，，步长[::步长]默认步长是1!
name.append("hahahaa")
name.insert(2, "uuuuuuu")
name.remove("biubiubiu")
del name[0:2]
print(name)
# 1.4列表基本操作 追加list.append("") 插入到某个位置（如果指定倒数位置 将插入位置前面） list.insert(2,"") 删除list.remove("") del li[2]下标删除 切片删除(函数内无效)li=li[:] 弹出li.pop(index),,默认弹出最后一个
# 1.5列表判断 in 数量li.count() 找索引li.index()只会返回找到的第一个元素位置 列表长度,,len(li)
if "hahahaa" in name:
    num_of_sth = name.count("hahahaa")
    posistion = name.index("hahahaa")
    print("[%s] hahahaa in name.posistion is [%s]" % (num_of_sth, posistion))
# 1.6列表高端操作 拓展进一个新的列表 li.extend(li2) 反转列表li.reverse() 排序li.sort(),,python3数字和字符串排序会报错,,python2会按asc2码的顺序来排 拷贝li.copy() 枚举enumerate()
name2 = ["babababa", "hehehehe", "niuniuniu"]
name.extend(name2)
name.reverse()
# name.sort()
# 1.7列表注意！！ 列表直接赋值是整个列表指引,,li=li2,,改变一个都会变 所以要用copy 但是copy为浅拷贝!!,,意思是被拷贝的列表里有嵌套列表,用copy后嵌套的列表依然为指引 如果要深拷贝,,请用copy库的deepcopy
name.append([1, 2, 3, 4, 5, 6])
nameShallowcopy = name.copy()
nameTruecopy = copy.deepcopy(name)

# 2.1元组truple 只读列表 元组不可更改 truple.count() truple.index()
r = (1, 2, 3, 4, 5)

# 3.1字符串操作 string.strip()默认脱空格换行tab,也可以指定   string.split(",")按指定符号拆分成列表,,string.join(列表)合并列表每个元素加入string ''in string判断有没有空格
username = 'year    '
username.strip()
usernames = 'uar,asdf,asdf,erg,erh'
username = usernames.split(',')
usernames = '|'.join(username)
print('' in usernames)
# 3.2字符串操作2 string.capitalize()首字母大写 string.format()格式化字符串,,推荐使用  字符串切片同列表  指定长度填充居中string.center(40,'-')  查找指定字符串string.find('')返回索引  string.isdigit()等等判断是否为某个类型   string.endswith()startswith()  string.upper().lower()
usernames.capitalize()
msgTamplte1 = "Hello, {name}, you are {age} years old!"
msgTamplte2 = "Hello, {0}, you are {1} years old!"
msg1 = msgTamplte1.format(name='year', age=23)
msg2 = msgTamplte2.format('year', 23)

usernames.center(50, '-')

usernames.find('uar')
print(usernames.isdigit())
usernames.endswith('ddd')
usernames.startswith('asdf')
usernames.upper().lower()
