#读取和写入行(功能是提供和接收数据)



f = open('somefile.txt', 'w')
print(f.write('Hello, '))
print(f.write('World!'))
print(f.close())


f = open('somefile.txt', 'r')
print(f.read(4))  #指定要读取多少（ 4）个字符
print(f.read())

  


#计算sys.stdin中包含多少个单词的简单脚本
# somescript.py
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)



#使用read迭代字符
with open(filename) as f:
    for char in f.read():
        process(char)



#使用readlines迭代行
with open(filename) as f:
    for line in f.readlines():
        process(line)




'''
    使用f.write来写入数据，还可使用f.read来读取数据。

    在文本和二进制模式下，基本上分别将str和bytes类用作数据。

    调用f.write(string)时，你提供的字符串都将写入到文件中既有内容的后面。

    调用open时，原本可以不指定模式，因为其默认值就是'r'。

    除进行迭代外，像这样将文件内容读取到字符串或列表中也对完成其他任务很有帮助。

    使用 fileinput 实现延迟行迭代有时候需要迭代大型文件中的行，此时使用readlines将占用太多内存。

    转而结合使用while循环和readline，在Python中，在可能的情况下，应首选for循环，而这里就属于这种情况。




'''
