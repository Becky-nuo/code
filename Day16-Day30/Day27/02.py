#socket TCP通信(客户端程序）

import socket

client = socket.socket()  #实例初始化

ip_port = ("127.0.0.1",8888)  #访问的服务器的IP和端口

client.connect(ip_port)  #连接主机

data = client.recv(1024)  #接收主机信息，1024表示：接收数据1024个字节

print(data.decode()) #打印接收的数据
''' python3.x以上，网络数据的发送接收都是bety类型
    如果发送数据时str类型的则需要进行编码  '''


print(data.decode())  #

while True:  # 定义一个循环

    data = client.recv(1024)  #连接主机

    print(data.decode())  #打印接收数据

    m_input = input("输入发送的消息：")  #输入发送的消息

    client.send = (m_input.encode())  #消息发送
    if m_input == "exit":
        break

    data = client.recv(1024)

    print(data.decode())
