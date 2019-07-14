#python中完善decorator


import time,functools

def performance(unit):
    def f1(f):
        @functools.wraps(f)
        def f2(n):
            print('call',f1.__name__+'()in',f(n),unit)
            return f(n)
        return f2
    return f1

@performance('ms')
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print(factorial.__name__)
'''
    @decorator可以动态实现函数功能的增加
'''




def log(f):
    def wrapper(*arg,**kw):
        print('call...')
        return f(*arg,**kw)
    return wrapper
@log
def f2(x):
    pass
print(f2.__name__)
'''
    由于decorator返回的新函数函数名已经不是‘f2’，/
而是@log内部定义的‘wrapper’，函数名的代码就会失效。/
decorator还改变了函数的__doc__等其它属性。
'''
