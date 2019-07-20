#socket upd通信(服务器端程序)

import socket

k = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建实例，IPV4的方式

ip_port = ("127.0.0.1",8888) #

k.bind(ip_port)  #绑定监听

while True:  #循环

    data = k.recv(1024)  #接收数据

    print(data.decode())  #打印数据
