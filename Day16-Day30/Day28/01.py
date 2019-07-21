#socket非阻塞模块

import socketserver
import random

class MyServer(socketserver.BaseRequesHandler):  #定义一个类
'''如果handle方法出现报错，则会进行跳过
    setup方法和finish方法无论如何都会进行执行的 '''
    
    def setup(self):  #首先执行setup
        pass

    def handle(self):  #然后执行handle

        conn = self.request  #
        m = "Hello World!"  #
        conn.send(m)  #
        while True:
            data = conn.recv(1024)  #接收客户端信息
            print(data.decode())  #打印信息

            if data = b'exit':  #接收到exit则进行循环的退出
                break

            conn.send(data)
            conn.send(str(random.randint(1,1000)).encode())  #
            conn.close()  #关闭连接对象
        

    def finish(self):  #最后执行finish
        pass


if __name__ == "__main__":

    server = socketserver.ThreadingTCPServer(("127.0.0.1",8888),MyServer)#创建多线程实例

    server.server_forever() #开启异步多线程，等待连接
