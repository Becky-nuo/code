 a = 5
>>> a
5
>>> id(5)
1428251808
>>> type(5)
<class 'int'>
>>> b = "小明"
>>> id(a)
1428251808
>>> type(a)
<class 'int'>
>>> id(b)
63692528
>>> type(b)
<class 'str'>


'''
  1、id:1428251808：type(类型):int，value(值):3
      id(b):63692528：type:str，value:小明
  2、python中，一切皆对象
  3、本质：一个内存条，拥有特定的值，支持特定类型的相关操作
  4、堆（对象）：ID、type、value
     栈（变量）
