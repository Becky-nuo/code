#os(能够访问多个操作系统服务)

'''

模块os函数和变量函数:

        变量                          描 述
    environ                     包含环境变量的映射
    system(command)             在子shell中执行操作系统命令
    sep                         路径中使用的分隔符pathsep 分隔不同路径的分隔符
    linesep                     行分隔符（ '\n'、 '\r'或'\r\n'）
    urandom(n)                  返回n个字节的强加密随机数据


    映射也可用于修改环境变量，但并非所有的平台都支持这样做。函数os.system用于运行外部程序。
    
    变量os.sep是用于路径名中的分隔符。
    
    使用os.pathsep来组合多条路径。
    
    pathsep用于分隔不同的路径名。
    
    变量os.linesep是用于文本文件中的行分隔符。
    
    os.startfile接受一个普通路径，即便该路径包含空白也没关系。

    这里用引号将Program Files和Mozilla Firefox括起来了，否则，底层shell将受阻于空白处。
    
    在Windows中，使用os.system或os.startfile启动外部程序后，当前Python程序将继续运行；
而在UNIX中，当前Python程序将等待命令os.system结束。


'''
