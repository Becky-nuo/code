#socket TCP通信（服务器端程序）

import socket   #导入模块

s = socket.socket()   #创建实例

ip_port = ("127.0.0.1",8888)  #定义绑定IP和port

s.bind(ip_port)  #绑定监听

s.listen(5)   #最大连接数

print("正在进行等待接收数据....")  #提示信息

conn,address = s.accept()  #接收数据

m = "hello world!"  #定义信息

conn.send(m.encode())  #返回信息,encode()就是编码
''' python3.x以上，网络数据的发送接收都是byte类型
    如果发送数据时str类型的则需要进行编码  '''

conn.close()  #主动关闭连接


'''
    socket是什么：
        socket是电脑网络中进程间数据流的端点。
        socket操作系统的通信机制。
        应用程序通过socket进行网络数据传输。

    socket通信方式：
        socket分为UDP和TCP两种不同的通信方式

    为什么是socket：
        socket能够适应多种网络协议。
        socket是基础应用，了解socket可以举一反三。
        服务器传输大量涉及网络协议，离不开socket应用。
'''
