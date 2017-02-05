# -*- coding:utf-8 -*-
# Author:YEAR
# 设计模式跟语言没有关系,是设计代码结构的方式,方便更好的添加修改代码
# 设计模式1:单例模式,,只有一个实例
# 当每个对象中封装了不同的数据的时候,我们需要创建多个实例不适用于单例模式
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


xiaoming = Person('haha', 18)
xiaor = Person('jiujiu', 19)


# 这种情况就适用单例模式,你创建再多个对象都是一样的
class Person1:
    def __init__(self):
        self.name = 'haha'
        self.age = 18

    def f1(self):
        pass

    def f2(self):
        pass


xiaoming = Person1()
xiaoming.f1()


# 在程序于数据库交互的时候,要链接操作断开,但链接的时间远远超过操作时间,所以有了数据库连接池.

class ConnectionPool:
    def __init__(self):
        self.ip = '1.1.1.1'
        self.port = 3306
        self.pwd = '123123'
        self.username = 'root'

        self.conn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_connection(self):
        # 获取链接
        import random
        r = random.randrange(1, 11)
        return r


pool = ConnectionPool()  # 我们只需要一个链接池就够了 单例

for i in range(10):
    print('获取链接')
    conn = pool.get_connection()
    print('获取的是', conn)

# 但是不同的人用的时候还是会创建多个实例
for i in range(10):
    pool = ConnectionPool()
    print('获取链接')
    conn = pool.get_connection()
    print('获取的是', conn)


# 要保证,每次创建只拿到同一个实例
class ConnectionPool1:
    __instance = None

    def __init__(self):
        self.ip = '1.1.1.1'
        self.port = 3306
        self.pwd = '123123'
        self.username = 'root'

        self.conn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @staticmethod
    def get_instance():
        if ConnectionPool1.__instance:
            return ConnectionPool1.__instance
        else:
            ConnectionPool1.__instance = ConnectionPool1()
            return ConnectionPool1.__instance

    def get_connection(self):
        # 获取链接
        import random
        r = random.randrange(1, 11)
        return r
