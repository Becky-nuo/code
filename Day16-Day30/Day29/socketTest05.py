#Python实现socket的非阻塞式编程


from socket import *
serSocket = socket(AF_INET, SOCK_STREAM)#建立套接字
localAddr = ('', 7789)

serSocket.bind(localAddr)#为其绑定本机信息
serSocket.setblocking(False)#将tcp套接字转化为非阻塞式
serSocket.listen(5)#将套接字变为被动监听
clientAddrList = []#用来存储所有客户端的信息

while True:
    #print("---wait for client---")
    try:
        newSocket, clientAddr = serSocket.accept()
    except:
        pass
    else:
        print('---new client [%s]'%(str(clientAddr)))
        
        newSocket.setblocking(False)#为了不令接收到的客户端套接字陷入阻塞状态，将客户端套接字也转为非阻塞
        clientAddrList.append((newSocket, clientAddr))
        '''因为引用计数器的关系，每一次循环的执行都会使newSocket变为新的对象，newSocket无法在接下来使用，应将其存在列表里'''
    for newSocket, clientAddr in clientAddrList:
        try:
            recvDate = newSocket.recv(1204)
        except:
            pass
        else:
            if len(recvDate) > 0:
                print('---massage from [%s] is: %s---'%(str(clientAddr), recvDate.decode('utf-8')))
            else:
                print('---client was closed---')
                newSocket.close()
                clientAddrList.remove((newSocket, clientAddr))
                

'''
    1、python 的单进程服务器一次只能处理一个客户端，但我们可以将单进程服务器变为非阻塞式，增加实用价值
    2、利用socket中的setblocking()方法可以处理多个客户端，且不会相互影响

'''
