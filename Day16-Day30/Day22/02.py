#python 中动态导入模块

try:
    import simplejson as json
except:
    import json as json

print(json.dumps({'python':3.7}))




try:
    import json
except ImportError:   #利用ImportError经常在python中动态导入模块
    import simplejson as json

print(json.dumps({'python':2.7}))


'''
    1、有的时候，两个不同的模块提供了相同的功能
    2、python是动态语言，解释执行，因此python代码执行速度慢。
    3、要提高python代码的运行速度，把某些关键函数用C语言重写，能提高执行速度。
    4、try的作用是捕获错误，并在捕获到指定错误执行except语句
    
'''
