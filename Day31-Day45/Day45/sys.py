#sys

'''

sys模块sys让你能够访问与Python解释器紧密相关的变量和函数

       变量                   描 述
    argv              命令行参数，包括脚本名
    exit([arg])       退出当前程序，可通过可选参数指定返回值或错误消息
    modules           一个字典，将模块名映射到加载的模块
    path              一个列表，包含要在其中查找模块的目录的名称
    platform          一个平台标识符，如sunos5或win32
    stdin             标准输入流——一个类似于文件的对象
    stdout            标准输出流——一个类似于文件的对象
    stderr            标准错误流——一个类似于文件的对象

    变量sys.argv包含传递给Python解释器的参数，其中包括脚本名。
    函数sys.exit退出当前程序。(try/finally块中调用它时， finally子句依然会执行)你可向它提供一个整数，指出程序是否成功，这是一种UNIX约定。
    在大多数情况下，使用该参数的默认值（ 0，表示成功）即可。也可向它提供一个字符串，这个字符串将成为错误消息，对用户找出程序终止的原因很有帮助。
    程序退出时将显示指定的错误消息以及一个表示失败的编码。映射sys.modules将模块名映射到模块（仅限于当前已导入的模块）。
    

    变量sys.path在本章前面讨论过，它是一个字符串列表，其中的每个字符串都是一个目录名，执行import语句时将在这些目录中查找模块。
    变量sys.platform（一个字符串）是运行解释器的“平台”名称。是表示操作系统的名称（如sunos5或win32），也可能是表示其他平台类型的名称。
    变量sys.stdin、 sys.stdout和sys.stderr是类似于文件的流对象，表示标准的UNIX概念：标准输入、标准输出和标准错误。

    

    从命令行调用Python脚本时，你可能指定一些参数，也就是所谓的命令行参数。这些参数将放在列表sys.argv中，其中sys.argv[0]为Python脚本名。
按相反的顺序打印这些参数非常容易。


'''
#反转并打印命令行参数
# 文件名.py
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))


print(' '.join(reversed(sys.argv[1:])))



