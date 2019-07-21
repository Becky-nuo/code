#文件上传程序的编写（文件发送端）

import socket

s = socket.socket()   #实例化模块

ip_port = ('127.0.0.1',9999)  #定义连接IP和port

s.connect(ip_port)  #服务器连接

#文件上传(客户端上传到服务器端)
with open('02.py') as f:   #打开文件
    for i in f:   #按每一段分割文件
        s.send(i)  #数据上传
        data = s.recv(1024)  # 接收数据
        if data == b'success':  # 判断服务器端是否真正的接收成功
            break


s.send('quit'.encode())  #给服务器端发送结束信号


