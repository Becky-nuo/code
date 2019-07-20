#socket客户端连续消息发送


import socket   #导入模块
import random

s = socket.socket()   #创建实例

ip_port = ("127.0.0.1",8888)  #定义绑定IP和port

s.bind(ip_port)  #绑定监听

s.listen(5)   #最大连接数

while True:    #不断接收数据

    print("正在进行等待接收数据....")  #提示信息

    conn,address = s.accept()  #接收数据

    m = "连接成功！"  #定义信息

    conn.send(m.encode())  #返回信息,encode()就是编码
    ''' python3.x以上，网络数据的发送接收都是byte类型
        如果发送数据时str类型的则需要进行编码  '''

    while True:   #不断接收客户端发来的消息

        data = conn.recv(1024))  #接收客户端消息

        print(data.decode())  #打印数据

        if data == b'exit': #接收到退出命令
            break

        conn.send(str(random.randint(1,1000).encode())) #发送随机数消息

    conn.close()  #主动关闭连接
