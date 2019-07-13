#python中返回函数


def f():
    print 'call f()...'

    def g():  #定义函数g
        print 'call g()...'  #返回函数g

    return g
'''
    在函数f内部定义一个函数g。由于函数g是一个对象，/
函数名g就是指向函数g的变量，所以，最外层函数f可以返回变量g，/
也就是函数g本身。

'''


'''区分返回函数和返回值'''
def myabs():
    return abs  #返回函数
def myabs2(x):
    return abs(x)  #返回函数调用结果，返回值是一个数值



'''用函数calc_prod(lst),接收一个lst,返回一个函数，返回函数可以计算参数的乘积'''
def calc_prod(lst):
    def lazy_prod():
        def f(x,y):
            return x*y
        return reduce(f,lst,1)
    return lazy_prod

f = calc_prod([1,2,3,4])
print(f)
