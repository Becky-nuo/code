# socket 服务器端

from socket import *
from time import ctime
HOST = '10.69.141.11'                        #主机(服务器)地址
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建套接字
tcpSerSock.bind(ADDR)                      # 监听
tcpSerSock.listen(5)
while True:
    print('wating for connection...')
    tcpCliSock,addr = tcpSerSock.accept()  #被动接收连接
    print('...connected from:',addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()#接收来自客户端的数据
        if  data=='exit':
            break
        print(data)                      #输出客户端的数据
        sersay=raw_input("what do you want to say")
        tcpCliSock.send('%s'% (sersay).encode()) #返回给客户端的数据   发送给客户端的代码必须编码
    tcpCliSock.close()
tcpSvrSock.close()
 

