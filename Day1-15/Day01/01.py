>>> my_name     #未赋值
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    my_name
NameError: name 'my_name' is not defined  #使用前必须被初始化（先被赋值）
>>> a = 5
>>> del a  #删除（栈删除，堆会被垃圾回收器回收）
>>> id(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    id(a)
NameError: name 'a' is not defined
>>> id(5)
1448174752
>>> type(5)
<class 'int'>
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined


'''
  1.使用前必须被初始化（先被赋值）
  2.如果对象没有变量引用，就会被垃圾回收器回收，清理内存空间
