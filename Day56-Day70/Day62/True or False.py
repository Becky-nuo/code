Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #布尔值（1表示False,0表示True）
>>> a=True
>>> b=2
>>> a+b
3
>>> 
>>> 
>>> #比较运算符（1表示真，0表示假）
>>> c=4
>>> d=5
>>> c<d   #小于
True
>>> c != b   #不等于
True
>>> c == d  #等于
False
'''
    >，大于
    >=,大于等于
    <=,小于等于
'''
    
    
 #逻辑运算符
>>> c=True
>>> d=False
>>> c or d    # 或  c为True是,则不计算d的值，直接返回True;c为False时，直接返回False
True
>>> c and d   # 与  c为True是,则返回d的值;c为False时，则不计算d的值,直接返回False。
False
>>> c not d   # 非  c为True是,返回False;c为False时，直接返回True。
False


#同一运算符(用于比较两个对象的单元，实际比较的是对象的地址)
>>> e=1000
>>> f=1000
>>> e==f
True
>>> e is f
False
>>> id(e)
68780464
>>> id(f)
68780448
'''
    is与==的区别：
    is用于判断两个变量引用的对象是否同一个（比较对象的地址）
    ==用于判断引用变量对象的值是否相等
'''

#整数缓存问题
>>> g=10
>>> h=10
>>> g is h
True
>>> id(g)
2011784432
>>> id(h)
2011784432

'''
    python仅仅对比较小的整数对象进行缓存（范围【-5,256】)起来，/
    并非所有整数对象，只对命令行执行。
    pycharm或者保存文件执行，结果会不一样，因为解释权做了一部分优化，\
    范围【-5,任意正整数】
'''

