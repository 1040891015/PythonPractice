# -*- coding:utf-8 -*-
import socket

server = socket.socket()  # 初始化
server.bind(('localhost', 6969))  # 绑定ip和端口

server.listen(5)  # 监听，设置最大数量是5
print("开始等待接受客户端数据----")
while True:
    conn, addr = server.accept()  # 获取客户端地址
    print(conn, addr)
    print("客户端来数据了")
    while True:
        data = conn.recv(1024)  # 接收数据
        print("接受的数据：", data)
        if not data:
            print("client has lost")
            break
        conn.send(data.upper())  # 返回数据

serve.close()  # 关闭socket

