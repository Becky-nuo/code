Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python把函数作为参数
 
>>> def add(x,y,f):
	return f(x) + f(y)

>>> add(-5,9,abs)    #传入abs作为参数的值
14                #abs(-5) + abs(9)



'''利用add(x,y,f)函数计算：根号x + 根号y'''

>>> import math
>>> def add(a,b,g):
	return g(a) + g(b)
>>> add(25,9,math.sqrt)
8.0

