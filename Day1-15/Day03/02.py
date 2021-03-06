Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#列表创建

#基本语法[]创建
>>> a=[10,20,30,"nuo"]  #列表可以存储任何数据
>>> a[0]  #
10
>>> a[3]
'nuo'
>>> a=[]  #创建一个空的列表对象
>>> a
[]
>>> a.append(20)  #增加元素
>>> a
[20]

#list()（可以将任何迭代的数据转化为成列表）
>>> a=list()  #创建空的列表对象
>>> a=list(range(10))     #字符转为列表
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=list("cvbfg")
>>> a
['c', 'v', 'b', 'f', 'g']

#range()   range([start],end,[step])
>>> list(range(0,10,1))   #
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(3,20,2))
[3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> list(range(20,3,-1)) #从右往回数,
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]
'''
  start：可选，表示起始数字，默认为0；
  end  ：必选，表示结尾数字；
  step ：可选，表示步长，默认为1；
range()返回的是一个range对象，而不是列表，需要通过list()方法将其转换成列表对象。
'''
#推导式生成列表
>>> a=[x*2 for x in range(5)]  #循环创建多个元素  5：0到4  x*2：乘2
>>> a
[0, 2, 4, 6, 8]
>>> a=[x*2 for x in range(100)]
>>> a
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
>>> a=[x*2 for x in range(100) if x%9==0] #  导出能被9整除的元素
>>> a
[0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]





#列表元素的增加（数值拷贝）

#append()  原地修改列表对象，列表尾部添加新的元素，速度最快
>>> a=[20,30]
>>> a.append(40)   #增加新的元素
>>> a
[20, 30, 40]

#+运算符操作（不是真正的尾部添加元素，而是创建新的列表对象，会产生大量的复制操作）
>>> a=[20,40]
>>> id(a)
48338904
>>> a=a+[50]
>>> id(a)
1745624  #对象不一致，产生新对象，重新赋值给a

#extend() 所有元素添加到本地列表，属于原地操作，不创建新的列表对象，适合两个列表整合
>>> a=[20,40]
>>> id(a)
54787808
>>> a.extend([50,60])
>>> id(a)
54787808 #对象一致，在原有的对象中进行拼接
>>> a
[20, 40, 50, 60]

#insert() 可将指定的元素插入到对象的任意制定位置，但会将后面的所有元素进行移动，会影响处理速度
>>> a=[10,20,30]
>>> a.insert(2,100)  #将100插入到2的位置
>>> a
[10, 20, 100, 30] 

#乘法扩展（使用乘法扩展列表，生成新的列表。适用于乘法操作，还有：字符串、元组）
>>> a=["nmg",30]
>>> b=a*3  #乘法3次
>>> a
['nmg', 30]
>>> b
['nmg', 30, 'nmg', 30, 'nmg', 30]


#列表元素的删除（数值拷贝）

#del （删除列表指定位置元素）
>>> a=[10,20,30]
>>> del a[2]
>>> a
[10, 20]

#pop() 删除并返回指定位置元素，如未指定则默认删除最后一个位置元素，直至结束。
>>> a=[1,2,3,4,5,6,7,8]
>>> b=a.pop()
>>> b
8
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> c=a.pop(1)  #删除位置1的元素
>>> c
2
>>> a
[1, 3, 4, 5, 6, 7]

#remove() 删除首次出现的指定元素，若不存在该元素抛出异常
>>> a=[10,20,30,40,50,60]
>>> a.remove(20)
>>> a
[10, 30, 40, 50, 60]
>>> a.remove(100)  #不存在100这个元素
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.remove(100)
ValueError: list.remove(x): x not in list

