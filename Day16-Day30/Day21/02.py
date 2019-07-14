#python中编写带参数decorator


def log(prefix):
    def log_decorator(f):  #返回decorator
        def wrapper(*args,**kw):
            print('[%s] %s()....'%(prefix,f.__name__))
            return f(*args,**kw)
        return wrapper
    return log_decorator
@log('DEBUG')
def test():
    pass
print(test)



def performance(unit):
    def f1(f):
        def f2(n):
            print'call',f.__name__+'()in',fn((),unit
            return f1(f)
        return f(2)
    return f1

@performance（'ms'）
def factorial(n):
    return reduce(lambda x,y: x*y,range(1,n+1))
print(factorial(10))

