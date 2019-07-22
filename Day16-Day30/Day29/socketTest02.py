#socket客户端

from socket import *
HOST = '10.69.141.11'
PORT=20000 #IP地址一致，指向服务器地址PORT = 20000
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data= input()
    print("so %s old" %data )
    if  data=='exit':
        break
    tcpCliSock.send(data.encode())            #发送给服务器的数据
    data = tcpCliSock.recv(BUFSIZE).decode()  #接收数据
    if data=='exit':
        break
    print(data)
tcpCliSock.close()
