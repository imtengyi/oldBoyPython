# -*- coding:utf-8 -*-
# Author:YEAR
# 1.1函数
def f1():  # def关键字,创建函数 函数名 ()
    pass  # 函数体 返回值 默认返回值是none


# 1.2发送邮件函数
def sendMail():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText('内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["YEAR", 'yearzhou93@gmail.com'])
        msg['To'] = formataddr(["揍你", '243132373@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.gmail.com", 25)
        server.login("yearzhou92@gmail.com", "year93926")
        server.sendmail('yearzhou92@gmail.com', ['243132373@qq.com', ], msg.as_string())
        server.quit()
    except:
        return False
    else:
        return True


ret = sendMail()
if ret:
    print('OK')
else:
    print('faild')


# 1.3函数变量
# 普通参数(严格按照顺序将实际参数传递给形式参数)
# 默认参数(必须放置到参数列表的最后)
# 指定参数(将实际参数赋值给指定的形式参数)
# * 动态参数 默认将传入的参数放入一个元组中 f(*[11,22,3,4])每一个元素
# ** 动态参数2 默认将传入的参数放入一个字典中 f(**['1':11,'asdf':123])
# 万能参数 f(*args,**kwargs) *在前**在后
# 函数的参数进行传递的时候是引用还是值  是引用！！！！
# 全局变量 作用域问题 所有作用域都可读!! 重新赋值得加上global关键词 特殊的是列表字典可修改但不能重新赋值因为是引用 全局变量大写约定俗成
def sendMail1(xxoo, content, xx='biubiubiu'):  # 形式参数和默认参数 默认参数必须要放到参数列表最后!!!
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["YEAR", 'yearzhou93@gmail.com'])
        msg['To'] = formataddr(["揍你", '243132373@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.gmail.com", 25)
        server.login("yearzhou92@gmail.com", "year93926")
        server.sendmail('yearzhou92@gmail.com', [xxoo, ], msg.as_string())
        server.quit()
    except:
        return False
    else:
        return True


ret = sendMail1('243132373@qq.com', 'SB')  # 普通参数 默认参数

while True:
    em = input("输入邮箱地址:")
    ret1 = sendMail1(em, 'SB')
    if ret:
        print('ok')
    else:
        print('doubi')

sendMail1(content='jjj', xxoo='jjj')  # 指定参数传参


def f2(*args):  # 将接收的n个参数放到一个元组李里
    print(args)


f2(11, 22, 33, 44, 'asdfasdf')
li = [11, 22, 33, 44, 55, 'asdfasdf']
f2(li)  # 将此列表作为元组的一个元素
f2(*li)  # 将此列表所有元素作为元组的一个元素 *其实是对li做一个循环将每个元素分离出来


def f3(**args):  #
    print(args, type(args))


f3(name='year')  # 传入键值对作为字典
dic = {'name': 'year', 'age': 23}
f3(kk=dic)  # 将dic作为一个元素
f3(**dic)  # **可以循环将dic里的每一个键值对分离出来


def f4(*args, **kwargs):  # 万能参数
    print(args)
    print(kwargs)


# string的format格式化输出
a = 'i am {0},age{1}'.format(*["alex", 234])
b = 'i am {name},age{age}'.format(**{'name': 'year', 'age': 123})


# 函数的参数进行传递的时候是引用还是值  是引用！！！！
def f5(list1):
    list1.append(999)


li = [111, 222, 333, 444]
f5(li)
print(li)

# 全局变量
name = 'year'


def f6():
    # name = 'jiujiujiu'
    global name
    name = 'jiujiujiu'
    # 特殊情况 列表字典
    li.append('adsf')  # 可修改
    global li  # 重新赋值得用global
    # li = 'jiujiujiu'


print(name)
