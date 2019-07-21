#文件上传程序的编写（文件接收端）

import socket

s = socket.socket()  #实例化

ip_port = ('127.0.0.1',9999) #ip端口
 
s.bind(ip_port)  #绑定ip和port

s.listen(5) #最大连接数

while True:  #循环
    conn,address = s.accept() #等待客户端连接

    while True:    #一直使用当前连接进行数据发送，直到结束标志出现

    with open("file","ab") as f: #打开文件等待数据写入
        data = conn.recv(1024)  #接收数据

        if data == b'quit':
            break
            f.write(data)  #写入文件

    print('文件接收完成')  #打印提示信息


s.close()  #关闭连接
