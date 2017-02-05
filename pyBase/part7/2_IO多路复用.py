# -*- coding:utf-8 -*-
# Author:YEAR
# IO多路复用
# 通过一种机制,可以监视多个描述符,一旦某个描述符就绪,就可以感知到
# 这是系统底层实现的,和python没什么关系
# 系统底层有三种IO多路复用方式,select,poll,epoll
# poll对监听的描述符个数没有限制 和select一样都是for循环
# epoll就不一样了,不用for循环了,用异步方式,谁有变化谁站出来 nginx
import socket

address1 = ('127.0.0.1', 8001)
address2 = ('127.0.0.1', 8002)

sk1 = socket.socket()
sk1.bind(address1)
sk1.listen()

sk2 = socket.socket()
sk2.bind(address2)
sk2.listen()

inputs = [sk1, sk2]
outputs = []
message_dict = {}
import select

while True:
    # 第一个参数,内部会自动监听列表内所有对象,一旦发生变化
    # 如果有人连接sk1 则 r_list=[sk1],其他情况同理
    # 第四个参数,时间秒数,最长等待秒数,如果超过这个时间就跳过这句,返回空.
    # 第三个参数,列表内的描述符如果有错误就会感知到,会放进e_list返回,一般用来将出错的描述符从正常监听范围里去除
    # 第二个参数,只要是列表内的描述符,都会放进w_list返回,不管发生任何事情
    r_list, w_list, e_list = select.select(inputs, outputs, [], 1)
    print(r_list)
    for sk in r_list:
        # 每连接来一个
        if sk == sk1:
            # 表示有新客户端来链接
            conn, address = sk.accept()
            inputs.append(conn)
            message_dict[conn] = []
            # conn.sendall(bytes('Hello', encoding='utf-8'))
            # conn.close()
        else:
            # 表示有老客户发消息
            try:
                data = str(sk.recv(1024), encoding='utf-8')
            except Exception as e:
                # 如果用户关闭连接,,如果客户端直接关闭读取会报错这样就会跳进来.
                inputs.remove(sk)
            else:
                # 向用户发送消息
                # sk.sendall(bytes(data + '好!!!', encoding='utf-8'))
                message_dict[sk].append(data)
                outputs.append(sk)

    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes('Hello' + recv_str, encoding='utf-8'))
        outputs.remove(conn)

# 多线程
import time
import threading


def process(arg):
    time.sleep(1)
    print(arg)


for i in range(10):
    process(i)

for i in range(10):
    t = threading.Thread(target=process, args=(1,))
    t.start()
