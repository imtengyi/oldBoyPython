# -*- coding:utf-8 -*-
# Author:YEAR

class Foo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print('show')


# 反射 :以字符串形式去对象(模块)中操作成员
# 可以用于类中,只能找类成员,找不了对象成员
r = hasattr(Foo, "show")
print(r)
# 查看类成员
print(Foo.__dict__)

# 同样也可以用于对象,既可以找对象成员又可以找类成员,,因为对象中有类对象指针,
obj = Foo('biubiubiu')
print(hasattr(obj, 'name'))
print(hasattr(obj, 'show'))  # 通过对象中的类对象指针找到


# 静态字段,,类中,区别于普通字段,,,适用于每个对象中重复使用且值大多相同的情况


class enene:
    country = 'China'  # 静态字段 类中

    def __init__(self, name):
        self.name = name  # 普通字段,对象中

    def show(self):  # 普通方法,类中
        print('show')


print(enene.country)
obj = enene('niuniu')
enene.show(obj)  # 可以这么用,但最好不要这么写


# 规范:自己去访问自己的资源除了类中的方法,普通字段用对象去访问,静态字段用类去访问.

# 静态方法,内置函数中有一个staticmethod()这是一个装饰器.静态方法可以不用创建对象直接通过类调用
class enene1:
    country = 'China'  # 静态字段 类中

    def __init__(self, name):
        self.name = name  # 普通字段,对象中

    @staticmethod
    def show():  # 静态方法,类中
        print('show')


# 通过类调用静态方法
enene1.show()


# 类方法,内置函数中有一个classmethod()这是一个装饰器,必须要有一个cls参数,调用时会自动传递调用类给这个参数
class enene2:
    country = 'China'  # 静态字段 类中

    def __init__(self, name):
        self.name = name  # 普通字段,对象中

    @classmethod
    def show(cls):  # 静态方法,类中
        print('show')


# 只能通过类访问
enene2.show()


# 特性,将方法伪造成一种字段,除了self不能有参数
class enene3:
    country = 'China'  # 静态字段 类中

    def __init__(self, name):
        self.name = name  # 普通字段,对象中

    @property
    def show(self):  # 特性,可以不用括号来掉用函数
        print('show')
        return 'ha'


obj = enene3('haha')
print(obj.show)


# 像设置字段一样设置特性
class enene4:
    country = 'China'  # 静态字段 类中

    def __init__(self, name):
        self.name = name  # 普通字段,对象中

    @property
    def show(self):  # 特性,可以不用括号来掉用函数
        print('show')
        return 'ha'

    @show.setter  # 当需要设置特性的时候将调用被此装饰器装饰的函数,名字要统一
    def show(self, value):
        print(value)


obj = enene4('haha')
print(obj.show)
obj.show = 123


# 总结来说 面向对象三大特性:封装,继承,多态
# 成员:字段: 静态字段(每个对象都有一份),普通字段(每个对象都有不同的数据)
#     方法: 静态方法(无需使用对象封装的内容),类方法,普通方法(使用对象中的数据)
#     特性: 普通特性(将方法伪造成字段)


# 成员修饰符

# 加双下划线的静态字段和普通字段,被修饰为私有字段,只能被内部函数调用
class Boo:
    ox = 'hahah'
    __ox = 'ox'

    def __init__(self):
        self.__name = 'year'
        pass

    def fetch(self):
        print(Boo.__ox)


print(Boo.ox)
print(Boo.__ox)  # 报错


# 子类中同样不能访问私有字段
class Bar(Boo):
    def fetch(self):
        pass


obj = Bar()


# 对于方法同样 加了双下划线被修饰为私有函数

# 要想访问私有成员用_类名__成员名,不要这样用

# 面向对象内部方法 像__init__() __del__()这种
# __call__ 方法 当直接在对象后面加()的时候会调用
class Boo2:
    def __init__(self):
        print('hahahah')

    def __call__(self, *args, **kwargs):
        print('hahahah')
        return 1


obj = Boo2()
obj()
r = Boo2()()  # 会拿到__call__的返回值


# 用一切皆对象的想法去思考为什么字典对象后面可以加中括号,而我们自己创建的类对象不行
# __getitem__,,用中括号的时候会使用
class Boo3:
    def __init__(self):
        print('hahahah')

    def __call__(self, *args, **kwargs):
        print('hahahah')
        return 1

    def __getitem__(self, item):
        print(item)


# 人家字典对象还可以用中括号赋值,
# __setitem__,,赋值的时候调用
class Boo4:
    def __init__(self):
        print('hahahah')

    def __call__(self, *args, **kwargs):
        print('hahahah')
        return 1

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)


r = Boo4()
r()
print(r['hahaha'])
r['hahahah'] = 'jiujiujiu'


# 人家字典还可以用中括号删除
# __delitem__ 删除中括号时调用
class Boo5:
    def __init__(self):
        print('hahahah')

    def __call__(self, *args, **kwargs):
        print('hahahah')
        return 1

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


r = Boo5()
r()
print(r['hahaha'])
r['hahahah'] = 'jiujiujiu'
del r['hahahah']

# 人家列表对象还可以用切片
# 切片操作时py2.7会执行__getslice__方法 而py3中还是调用__getitem__
# 会将切片内容封装到一个对象中作为一个整体传给__getitem__
# 对于切片赋值和删除 一样py2.7会执行__setslice__方法 而py3中还是调用__setitem__

# 适当弄清楚类中__dict__所展示的所有成员的含义
r = Boo5()
print(r.__dict__)
print(Boo5.__dict__)


# 当我们for循环一个对象的时候
# for循环一个对象的时候会自动调用__iter__方法,生成器
class Boo6:
    def __iter__(self):
        yield 1
        yield 2
        yield 3


obj = Boo6()

for i in obj:
    print(i)


# print一个对象会调用__str__方法,返回什么东西就print什么东西





# 哈哈哈哈 一切皆对象,,所以类也是对象
# 默认来说来说类对象是通过type类创建
# 可以标记让谁来创建这个类 用__meateclass__=xxx来表示要谁来创建这个类,xxx为type的派生类

# type类的构造方法创建类
def func(self):
    print('jiujiujiu')


Foo = type('Foo', (object,), {'func': func})

# 当我们用类创建实例的时候会加括号调用,实际上就是调用了type类的__call__方法
