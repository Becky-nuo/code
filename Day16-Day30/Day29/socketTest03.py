#套接字函数

#服务端套接字函数
    import socket
    phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 1.服务端套接字函数
    phone.bind('主机ip地址',端口号)  #绑定到（主机，端口号）套接字
    phone.listen() #开始TCP监听
    phone.accept() #被动接受TCP客户的连接，等待连接的到来


#客户端套接字函数
    import socket
    phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#买手机
    phone.connect()  #主动连接服务端的ip和端口
    phone.connect_ex()  #connect()函数的扩展版本，出错的时候返回错码，而不是抛出异常


#服务端和客户端的公共用途的嵌套字函数
    phone.recv() #接受TCP数据
    phone.send() #发送TCP数据
    phone.recvfrom() #接受UDP数据
    phone.sendto() #发送UDP数据
    phone.getpeername() #接收到当前套接字远端的地址
    phone.getsockname() #返回指定套接字的参数
    phone.setsockopt() #设置指定套接字的参数
    phone.close() #关闭套接字


#面向锁的套接字方法# -*- coding: UTF-8 -*-
# python使用select进行非阻塞模式编程，客户端程序
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # 生成socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 不经过WAIT_TIME，直接关闭
sock.setblocking(False)                                     # 设置非阻塞编程

try:
    # sock.connect(("google.com", 80))
    sock.connect(("192.168.1.106", 789))
except Exception as e:
    print(e)

r_inputs = set()
r_inputs.add(sock)
w_inputs = set()
w_inputs.add(sock)
e_inputs = set()
e_inputs.add(sock)



    phone.setblocking()  #设置套接字的阻塞与非阻塞模式
    phone.settimeout()  #设置阻塞套接字操作的超时时间
    phone.gettimeout()  #得到阻塞套接字操作的超时时间


#面向文件的套接字函数
    phone.fileno()  # 套接字的文件描述符
    phone.makefile() #创建一个与该套接字相关的文件
