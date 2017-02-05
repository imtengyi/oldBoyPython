# -*- coding:utf-8 -*-
# Author:YEAR
# 面向过程编程
# 函数式编程
# 面向对象编程
# 像java,c#只能用面向对象编程
# python和Ruby可以用函数式编程和面向对象编程
class biubiubiu:
    def zouni(self, bbb):
        print(bbb)

    def huilai(self, bbb):
        print(bbb)


# 创建对象
obj = biubiubiu()
obj.zouni('lailailai')


# 类对象指针,在内存中的对象中会有个指向类的指针表名这个对象是由哪个类创建的
# 在调用对象中的方法的时候,会根据类对象指针找到类中的方法然后将对象自身传递给self参数.



# 封装,不用一个一个的传参了,在对象中存变量,调用的时候通过self拿到,这样就封装了变量,面向对象的优势就体现出来了,例如数据库的操作
class jiujiiujiu:
    def zouni(self):
        print(self.bbb)

    def huilai(self, bbb):
        print(bbb)


obj1 = jiujiiujiu()
obj1.bbb = 'hahaha'  # 封装的非主流方式
obj1.zouni()


# 封装的主流方式

# 当创建类的时候会调用__init__()方法,,构造方法
class enenen:
    def __init__(self, name, password):
        # 普通对象
        self.name = name
        self.password = password
        print('init')

    def __del__(self):
        pass


obj2 = enenen('year', '123')  # 初始化


# 在对象被销毁的时候会调用__del__()这叫析构函数,python有垃圾回收机制会自动调用 我们一般不要写

# 类类似模板每个对象封装的数据是不同的

# 类的继承

# 基类
class Animals:
    def chi(self):
        print('chi')

    def he(self):
        print('he')

    def piao(self):
        print('yaopiao')


# 派生类
class dog(Animals):
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print(self.name, 'wang!!')

    def piao(self):
        print('buyaopiao!!')


biubiu = dog('solon')
biubiu.jiao()


# 当派生类和基类中都存在的方法默认用派生类的.

# python允许多重继承, 优先级是自己然后从左到右排
class baba:
    def du(self):
        print('du')

    def piao(self):
        print('zouni')


class erzi(Animals, baba):
    def he(self):
        print('laiwan')


jiujiu = erzi()
jiujiu.piao()


# 当最顶层有共同父类的时候会最后找这个共同父类 3.5里是这样

# python的多态,python原生支持多态,因为python在创建对象或者传递对象的时候不需要指定类型,而其他语言需要.
def lalala(arg):  # 你可以传递任意类型的对象给arg 多态
    arg.zouni()


# python不支持重载


# 注意当类函数内还有调用其他类函数的时候,在继承时的调用情况,,,认清self的本质就好去判断了.

# 执行父类的构造方法,常用于面向对象,,
class erzi1(Animals):
    def __init__(self):
        super(erzi1, self).__init__()  # 调用父类的构造方法
        self.baba = 'jiujiu'
        # Animals.__init__(self) #这样也可以,但写死了,

# 关键还是认清self的本质 多看源码,,多找源头.
