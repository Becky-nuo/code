#map()函数


a=(1,2,3,4,5,6)
b=[1,2,3,4,5,6]
c="lh"


la=map(str,a)
lb=map(str,b)
lc=map(str,c)


print(a)
print(b)
print(c)


def f(x):
    return x ** 2  #计算平方数

d=list(map(f,[1,2,3,4,5]))  #计算列表各个元素的平方
print(d)


'''
    1、map()函数会根据提供的函数对指定序列做映射
    2、map()函数的语法：
        map(function,iterable,....)
        function:函数
        iterable:一个或多个序列
'''
