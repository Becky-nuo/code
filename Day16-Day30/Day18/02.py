#模块的导入（import）


import math

print(id(math))
print(type(math))
print(math.pi)  #通过math.成员名来访问模块中的成员



import math,turtle
'''一个模块无论导入多少次，模块在整个解释器进程内有且仅有一个对象'''
print(id(math))    


import math as m
print(id(m))



'''
    1、import 语句的基本语法格式如下：
            import 模块名     #导入一个模块
            import 模块1，模块2....    #导入多个模块
            import 模块名 as 模块别名   #导入模块并使用新名字


    2、import 加载的模块分为四个通用类别：
            a、使用python编写的代码（.py文件）
            b、已被编译为共享库或DLL的C或C++扩展
            c、包好一组模块的包
            d、使用C编写并连接到python解释器的内置模块
            
'''
