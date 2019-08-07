#fileinput(迭代一系列文本文件中的所有行)


'''
模块fileinput中一些重要的函数：

          函 数                                     描 述
    input([files[, inplace[, backup]]])     帮助迭代多个输入流中的行
    filename()                              返回当前文件的名称
    lineno()                                返回（累计的）当前行号
    filelineno()                            返回在当前文件中的行号
    isfirstline()                           检查当前行是否是文件中的第一行
    isstdin()                               检查最后一行是否来自sys.stdin
    nextfile()                              关闭当前文件并移到下一个文件
    close()                                 关闭序列


    调用脚本（假设是在UNIX命令行中）：$ python some_script.py file1.txt file2.txt file3.txt就能够依次迭代文件file1.txt到file3.txt中的行。
你还可在UNIX管道中对使用UNIX标准命令cat提供给标准输入（ sys.stdin）的行进行迭代。

    fileinput.input是其中最重要的函数，它返回一个可在for循环中进行迭代的对象。
    如果要覆盖默认行为（确定要迭代哪些文件），可以序列的方式向这个函数提供一个或多个文件名。
    还可将参数inplace设置为True（ inplace=True），这样将就地进行处理。
    对于你访问的每一行，都需打印出替代内容，这些内容将被写回到当前输入文件中。
    就地进行处理时，可选参数backup用于给从原始文件创建的备份文件指定扩展名。

    
    函数fileinput.filename返回当前文件（即当前处理的行所属文件）的文件名。
    
    函数fileinput.lineno返回当前行的编号。这个值是累计的，因此处理完一个文件并接着处理下一个文件时，
不会重置行号，而是从前一个文件最后一行的行号加1开始。

    函数fileinput.filelineno返回当前行在当前文件中的行号。每次处理完一个文件并接着处理下一个文件时，
将重置这个行号并从1重新开始。

    函数fileinput.isfirstline在当前行为当前文件中的第一行时返回True，否则返回False。
    
    函数fileinput.isstdin在当前文件为sys.stdin时返回True，否则返回False。
    
    函数fileinput.nextfile关闭当前文件并跳到下一个文件，且计数时忽略跳过的行。

    慎用参数inplace，因为这很容易破坏文件。
    

    如果每个文件包含的单词都是按顺序排列的，而你要查找特定的单词，则过了这个单词所在的位置后，就可放心地跳到下一个文件。
函数fileinput.close关闭整个文件链并结束迭代。

    rstrip是一个字符串方法，它将删除指定字符串两端的空白，并返回结果

'''

#fileinput使用示例。假设你编写了一个Python脚本，并想给其中的代码行加上行号。

#在Python脚本中添加行号
# 文件名.py
import fileinput
for line in fileinput.input(inplace=True):
    line = line.rstrip()
     num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))




添加行号后的行号添加程序
# numberlines.py
import fileinput
for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))



