# -*- coding:utf-8 -*-
# Author:YEAR
# 网络编程
# socket套接字,基于TCP,IP协议的一个包装,让我们专注于最上层.
# python中socket支持tcp,udp和进程间通信.


# 服务端,,先运行起来等待别人来链接,,需要指定一个ip和端口
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))  # 用元组列表的时候最好在最后加个逗号,为了与函数调用分开
sk.listen(5)  # listen函数可以传递一个值,表示最多阻塞数量,超过了就丢弃.

print('before')
conn, address = sk.accept()  # 接收客户端的请求,这一句会阻塞
# conn为和客户端的连接,address为客户端的地址信息
print('after')
print(conn, address)

# 这样会有一个问题,连接完一个程序就结束了,但是我们的需求是客户端永远在等待,永久循环来了
# 连接完了,我们还要发点东西 2.7里可以直接发字符串,但3里面要传字节
# 发完东西了得接收人家的回复了.
# 人家回复q就要退出,要不然没完没了了
while True:
    conn, address = sk.accept()
    conn.sendall(bytes('给你个飞天大草!!', encoding='utf-8'))
    while True:
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        if ret_str == 'q':
            break
        conn.sendall(bytes(ret_str + ' 好!!', encoding='utf-8'))
    print(address, conn)

# socket.socket()第一个参数是地址簇,可以用socket.AF_INET指用IPv4,,socket.AF_INET6指用IPv6,,socket.AF_UNIX指用于单一的unix系统进程间通信
# socket.socket()第二个参数是类型, socket.SOCK_STREAM指流式socket也就是TCP,,socket.SOCK_DGRAM指数据包式也就是UDP,,socket.SOCK_RAW指原始套接字,普通的无法处理类似ICMP等报文,这个可以
# sk.setblocking(bool) 是否阻塞,默认是阻塞的,如果设置成false,那么accept和recv都不阻塞了 会报错
# sk.connect_ex(),帮你做了错误处理
# sk.send()可能不会将指定内容全部发送,所以用sk.sendall()这个内部调用send()会全部发出
# sk.sendto()发送到指定地址
# sk.settimeout(timeout)设置套接字操作的超时期
# sk.getpeername()获取远程地址
# sk.getsockname()获取自己的地址
# sk.fileno() 套接字的文件描述符

# UDP服务端
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sk.bind(('127.0.0.1', 9999,))
while True:
    data = sk.recv(1024)
    print(str(data, encoding='utf-8'))

# 发这个要靠缓冲区,所以可能会有粘包现象,通过接收确认包来避免

# 处理并发 可以用socketserver模块 用的IO多路复用和多线程
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request,self.client_address,self.server
        pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999,), MyServer)
    server.serve_forever()
