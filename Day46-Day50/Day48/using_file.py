#使用文件的基本方法


#read(n)
f = open(r'文件路径.txt')
f.read(7)
f.read(4)
f.close()


#read()：
f = open(r'文件路径.txt')
print(f.read())
print(f.close())


#readlines()：
f = open(r'文件路径.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline(), end='')

print(f.close())



#readlines()：
import pprint
print(pprint.pprint(open(r'文件路径.txt').readlines())) #文件对象将被自动关闭这一事实


#write(string):

f = open(r'文件路径', 'w')
print(f.write('this\nis no\nhaiku'))
print(f.close())




#writelines(list)：

f = open(r'文件路径.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r'文件路径', 'w')
f.writelines(lines)
f.close()
