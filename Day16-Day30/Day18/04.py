#__import__()动态导入


s = "math"
m = __import__(s)   #导入后生成的模块对象的引用给变量m
print(s)


import importlib
a = importlib.import_module("math")
print(a.pi)



'''
    1、import语句本质上就是调用内置函数,可以通过__import__()实现动态导入，/
    给它动态传递不同的参数值。
'''
