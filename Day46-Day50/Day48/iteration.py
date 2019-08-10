

#迭代文件内容
def process(string):
    print('Processing:', string)


#每次一个字符（或字节）

#使用read遍历字符
with open(filename) as f: #将变量filename设置为实际使用的文件的名称。
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)



#不同的方式编写循环

with open(filename) as f:
    while True:
    char = f.read(1)
    if not char:
        break  #避免了重复的代码。
    process(char)

    



#在while循环中使用
readlinewith open(filename) as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)


#使用read迭代字符

with open(filename) as f:
    for char in f.read():
        process(char)


#使用readlines迭代行

with open(filename) as f:
    for line in f.readlines():
        process(line)

        

'''
    有用的实现包括将数据存储在数据结构中、计算总和、使用模块re进行模式替换以及添加行号。

     #process是虚构函数，对每个字符或行所做的处理，可以用自己的喜欢的方式实现这个函数。



     最简单（也可能是最不常见）的文件内容迭代方式是，在while循环中使用方法read。

     程序之所以可行，是因为到达文件末尾时，方法read将返回一个空字符串，但在此之前，
返回的字符串都只包含一个字符（对应于布尔值True）。

    只要char为True，就还没结束。


     如果你每次读取多个字符（字节），可指定要读取的字符（字节）数。

     每次一行处理文本文件时，你通常想做的是迭代其中的行，而不是每个字符。





'''
