#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import socket               # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = '0.0.0.0'  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接

while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    c.send('欢迎访问菜鸟教程！'.encode())
    while True:
        data = c.recv(1024)
        if not data:
            print('断了')
            c.close()
            break
        print(data)
        if data.decode().startswith('do'):
            time.sleep(10)
            c.send('ok'.encode())
    # c.close()  # 关闭连接