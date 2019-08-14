#使用 fileinput(实现延迟行迭代)


#使用fileinput迭代行
import fileinput
for line in fileinput.input(filename):
    process(line)


#文件迭代器    
#迭代文件
with open(filename) as f:
    for line in f:
        process(line)


for line in open(filename):
    process(line)



import sys
for line in sys.stdin:
    process(line)


f = open('somefile.txt', 'w')
print('First', 'line', file=f)
print('Second', 'line', file=f)
print('Third', 'and final', 'line', file=f)
print(f.close())

lines = list(open('somefile.txt'))
print(lines)

first, second, third = open('somefile.txt')
print(first)

print(second)
print(third)




'''
    模块fileinput会负责打开文件，你只需给它提供一个文件名即可。

    文件实际上是可迭代的，这意味着可在for循环中直接使用它们来迭代行。

    将文件用作了上下文管理器，以确保文件得以关闭。

    sys.stdin也是可迭代的，因此要迭代标准输入中的所有行。

    使用list(open(filename))）将其转换为字符串列表，其效果与使用readlines相同。



在示例中，需注意:

        使用了print来写入文件，这将自动在提供的字符串后面添加换行符。
        
        对打开的文件进行序列解包，从而将每行存储到不同的变量中。
        （这种做法不常见，因为通常不知道文件包含多少行，但这演示了文件对象是可迭代的。）

        写入文件后将其关闭，以确保数据得以写入磁盘。
        （如你所见，读取文件后并没有将其关闭。这可能有点粗糙，但并非致命的。）

'''
