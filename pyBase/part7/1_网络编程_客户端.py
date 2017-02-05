# -*- coding:utf-8 -*-
# Author:YEAR
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001,))

# 阻塞
result_bytes = obj.recv(1024)  # 最多接收1024字节 超出的下次接收会拿到
result_string = str(result_bytes, encoding='utf-8')
print(result_string)

while True:
    inp = input('请输入要发送的内容:')
    if inp == 'q':
        obj.sendall(bytes(inp, encoding='utf-8'))
        break
    else:
        obj.sendall(bytes(inp, encoding='utf-8'))
        ret = str(obj.recv(1024), encoding='utf-8')
        print(ret)

obj.close()

# UDP客户端
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    inp = input('请输入要发送的内容:')
    if inp == 'q':
        break
    sk.sendto(bytes(inp, encoding='utf-8'), ('127.0.0.1', 9999,))
sk.close()
