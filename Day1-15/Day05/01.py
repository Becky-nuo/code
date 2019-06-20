Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
  字典（字典的”键值对“的无序可变序列，每个元素都是一个“键值对”）
  "键"是任意的不可变数据（整数，浮点数，字符串，元组。列表字典、集合不能作为"键"，不可重复）
'''  



#字典的创建

#{}
>>> a={'name':'nuo','age':'19','job':'student'} #键可以是任意对象
>>> a
{'name': 'nuo', 'age': '19', 'job': 'student'}

#dict()
>>> b=dict(name='nuo',age=19)
>>> b
{'name': 'nuo', 'age': 19}
>>> b=[("name","nuo"),("age",19)]
>>> b
[('name', 'nuo'), ('age', 19)]
>>> c={}    #空的字典对象
>>> d=dict()  #空的字典对象

#zip()
>>> e=['name','age','job']  #"键"对象集合
>>> f=['nuo',19,'student']  #"值"对象集合
>>> g=dict(zip(e,f))  #整合
>>> g
{'name': 'nuo', 'age': 19, 'job': 'student'}


 
#字典元素的访问




#1.通过[键]获得“值”，若不存在，则报错
>>> a={'name':'nuo','age':'19','job':'student'}
>>> a['name']
'nuo'
>>> a['age']
'19'
>>> a['sex']  #不存在
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a['sex']
KeyError: 'sex'

#get()获得“值”。优点：指定键不存在，返回None,也可设定指定键不存在时默认返回对象。推荐使用get()获取“值对象”
>>> a.get('name')
'nuo'
>>> a.get('ddd') 
>>> a
{'name': 'nuo', 'age': '19', 'job': 'student'}
>>> a.get('ddd','不存在')  #指定默认返回值
'不存在'
>>> a.items()  #列出所有的键值对
dict_items([('name', 'nuo'), ('age', '19'), ('job', 'student')])
>>> a.keys()  #列出所有的键
dict_keys(['name', 'age', 'job'])
>>> a.values()  #列出所有的值
dict_values(['nuo', '19', 'student'])
>>> len(a)  #字典里面有多少对键值对
3
>>> 'name'in a  #是否在字典里面
True


#字典元素添加、修改、删除


#1.给字典新增“键值对”。如果“键”已存在，则覆盖旧的键值对，如不在，则新增。
>>> a={'name':'nuo','age':'19','job':'student'}
>>> a['address']='江西'  #新内容
>>> a['age']=20  #覆盖旧的键值对
>>> a
{'name': 'nuo', 'age': 20, 'job': 'student', 'address': '江西'}

#2.update(),新字典中所有键对值全部添加到旧字典对象上，如果key重复，则直接覆盖
>>> a={'name':'nuo','age':'19','job':'student'}  
>>> b={'name':'mnl','moeny':100,'sex':'女的'} #b直接覆盖给a
>>> a.update(b)
>>> a
{'name': 'mnl', 'age': '19', 'job': 'student', 'moeny': 100, 'sex': '女的'}


#3.字典中元素的删除

#del(),clear()删除所有键值对,pop()删除指定键值对，并返回对应的“值对象”
>>> a={'name':'nuo','age':'19','job':'student'}
>>> del(a['name'])
>>> a
{'age': '19', 'job': 'student'}  #已删除name
>>> b=a.pop('age')  #删除以后，同时返回键值对
>>> b
'19'

#4.popitem()随机删除和返回键值对（一个接一个地移除并处理项）。字典无顺序。
>>> a={'name':'nuo','age':'19','job':'student'}
>>> a.popitem()
('job', 'student')
>>> a
{'name': 'nuo', 'age': '19'}
>>> a.popitem()
('age', '19')
>>> a
{'name': 'nuo'}



#序列解包（可用于元组、列表、字典），可方便的对多个变量赋值
>>> x,y,z=20,30,10  #元组
>>> x
20
>>> y
30
>>> z
10
>>> s={'name':'nuo','age':'19','job':'student'}  #字典
>>> a,b,c=s   #默认对键进行操作
>>> a
'name'
>>> b
'age'
>>> c
'job'
>>> e,d,f=s.values() #对值进行操作
>>> e
'nuo'
>>> d
'19'
>>> f
'student'
>>> h,i,j=s.items()  #对键值对进行操作
>>> h
('name', 'nuo')
>>> i
('age', '19')
>>> h[0]    #解包
'name'
>>> h[1]    #解包
'nuo'
>>> 
 
