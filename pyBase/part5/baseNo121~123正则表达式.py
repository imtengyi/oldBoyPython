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

# match函数 从头开始匹配  将结果放入一个对象 通过对象的一些方法达到不同的功能 flag编译标志位
re.match('year', 'asdfengasdyearasdg').group()  # 返回re整体匹配的字符串 可以一次输入多个组号,对应组号匹配的字符串
re.match('year', 'asdfengasdyearasdg').start()  # 返回匹配开始位置
re.match('year', 'asdfengasdyearasdg').end()  # 返回匹配的结束位置 结束位置不包括
re.match('year', 'asdfengasdyearasdg').span()  # 返回元组 包括起始和结束位置
# search函数 找一个 将结果放入一个对象 通过对象的一些方法达到不同的功能 flag编译标志位


# finditer函数和 findall一样 只是返回值是一个iter对象

# sub函数 匹配替换 sub(pattern,repl,string, max=0) max为最大替换次数
re.sub("g.t", "have", "I get A,I got B, I get C")
# subn函数 和sub一样 只不过会列出替换次数
re.subn("g.t", "have", "I get A,I got B, I get C")
# split分割 只不过是按re规则分割
re.split('\d+', 'one1two2three3four4')
# compile函数 这个方法是Pattern类的工厂方法,用于将字符串形式的正则表达式便以为Pattern对象.第二个参数flag是匹配模式,取值可以使用按位或运算符'|' 可以把常用的正则表达式弄成对象重复使用提高效率
regex = re.compile(r'\w*oo\w*')
regex.findall('I have a Dream is Good and is cool')

# flag编译标志位
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别匹配
# re.M 多行匹配 影响^和$
# re.S 是.匹配包括换行符在内的所有字符
# re.U 根据Unicode字符集解析字符 影响\w\W\b\B
# re.X 该标志通过更理货的格式以便你将正则表达式的写的更易于理解

# 原生字符串加r python有自己的语法规则 例如python的转译
f = open("C:\abc.txt")  # 报错 \a为响铃符 正则也有自己的转译方式
re.search(r'\\year', 'asdfasdf\yearasdfasdfyearasdfasf').group()
re.search('\\\\year', 'asdfasdf\yearasdfasdfyearasdfasf').group()
# 这里为什么要用4个??  因为python调用的是re接口 re里有需要一层转译 2个反斜杠 python要对这两个反斜杠进行转译 所以需要4个

# 正则分组 去已经提取到的数据中再提取数据
r = re.match('h\w+', 'has asdfsdfsdf')
print(r.group())  # 获取匹配到的所有结果
print(r.groups())  # 获取模型中匹配到的分组结果
print(r.groupdict())  # 获取模型中匹配到的分组结果

r = re.match('h(\w+)', 'has asdfsdfsdf')
print(r.group())  # 获取匹配到的所有结果
print(r.groups())  # 获取模型中匹配到的分组结果
print(r.groupdict())  # 获取模型中匹配到的分组结果

r = re.match('h(?P<name>\w+)', 'has asdfsdfsdf')
print(r.group())  # 获取匹配到的所有结果
print(r.groups())  # 获取模型中匹配到的分组结果
print(r.groupdict())  # 获取模型中匹配到的分组结果

# findall 的分组
r = re.findall('h\w+', 'has asdf hal sdfsdf')
r = re.findall('h(w+)', 'hasaaabc asdf hal sdfsdf')  # 只拿分组里的结果给你
r = re.findall('h(w+)aa(ab)c', 'hasaaabc asdf hal sdfsdf')  # 列表中以元组为元素 元组里包含分组信息

# sub中有分组也没用
# split的分组 不加分组之前不匹配分割字符本身 加分组后会将分组内容也匹配到
re.split('year', 'asdfsdfyearasdfasdf', 1)
re.split('(year)', 'asdfsdfyearasdfasdf', 1)
