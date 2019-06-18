Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#元组tuple(不可变序列，不能修改元组中的元素)


#元组的创建

#通过()创建（小括号可以省略）
>>> a=(10,20,30)
>>> type(a)
<class 'tuple'>
>>> b=(20)
>>> type(b)
<class 'int'>
>>> b=(20,)  '''元组元素只有一个元素，后面必须加一个逗号/
（因为解释器会把（1）解释为整数1，（1,）解释为元组）'''
>>> type(b)
<class 'tuple'>  #类型

#通过tuple()创建元组（可迭代的对象）
>>> c=tuple()    #创建一个空元组对象
>>> c
()
>>> b=tuple("abcd")  #字符串转元组
>>> b
('a', 'b', 'c', 'd') 
>>> b=list("abcd")  #tuple与list用法几乎一样
>>> b
['a', 'b', 'c', 'd']
>>> b=tuple(range(3))  #range()对象
>>> b=tuple([2,3,4])  #列表对象转元组
>>> b
(2, 3, 4)
>>> del b  #元组对象删除
'''
  tuple()可以接收列表、其他序列类型、迭代器等生成元组
  list()可以接收元组、字符串、其他序列类型、迭代器等生成列表
  
'''

#元组元素访问和计数(元组的元素不能修改)
>>> a=(10,20,30,40)
>>> a[1]  #索引
20
>>> a[1]=100  #不能修改
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[1]=100
TypeError: 'tuple' object does not support item assignment
>>> a=tuple("abcdefghijklmnopq")  
>>> a
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q')
>>> a[1:10]  #切片
('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

#排序（元组只能使用sorted(),生成新的元组对象）
>>> b=(30,20,40)
>>> sorted(b)
[20, 30, 40]
>>> a=1,20  #元组
>>> b=30,20
>>> a+b  #拼接，生成新的元组对象
(1, 20, 30, 20)
>>> a
(1, 20)
>>> len(a)  #长度
2
>>> sum(a)  #集合
21
>>> max(a)  #提取最大值
20

#zip(将多个列表对应位置的元素组合成为元组，并返回zip对象) 
>>> a=40,50,60
>>> b=70,80,90
>>> c=10,20,30
>>> d=zip(a,b,c) #整合在一起
>>> d
<zip object at 0x00E09558> #生成zip对象
>>> list(d)    #元组转化成列表
[(40, 70, 10), (50, 80, 20), (60, 90, 30)]



#生成器推导式创建元组（使用小括号，生成的不是列表也不是元组，而是一个生成器对象）
>>> s=(x*2 for x in range(5))  #range(5):生成索引0到5的序列  for:循环
>>> s
<generator object <genexpr> at 0x011F8070>  #生成器
>>> tuple(s)  #通过tuple()包装，转化成元组
(0, 2, 4, 6, 8)
>>> tuple(s)  #使用生成器只能使用一次,第二次为空，需要再生成一次
()

##__next__0(两个下划线)
>>> s=(x*2 for x in range(5))
>>> s.__next__()
00
>>> s.__next__()
22
>>> s.__next__()
44
>>> s.__next__()
66
>>> s.__next__()
88
>>> s.__next__() #报错（没有内容）
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.__next__()
StopIteration

 
'''
	元组的核心特点：不可变序列
	元组的访问和处理速度比列表快
	与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键使用
'''
