#socket upd(客户端的程序)

import socket

k = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 创建实例

ip_port = ("127.0.0.1",8888) #

whlie True:   #循环
    m.input = input("输入发送消息：")  #输入发送的信息

    if m_input == "exit":  #退出循环条件
        break

    k.sendto(m_input.encode(),ip_port)  #数据发送

k.close()  #发送关闭信息
