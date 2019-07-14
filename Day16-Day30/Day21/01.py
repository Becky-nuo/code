#python中编写无参数decorator

#@log的定义
def log(f):
    def fn(x):    #装饰器函数
        print'call',f.__name__ + '()in',time.time()
        return f(x)
    return fn


#阶乘函数
import time
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print(factorial(10))


#参数不只一个的函数
@log
def add(x,y):  #需要传入两个参数，但@log写死了只含一个参数的返回函数
    return x+y
print((add(1,2)))



def log(f):
    def fn(*args,**kw): #*rgs和**kw 保证任意个数的参数总是能正常调用
        print'call'+ f.__name__ + '()...'
        return f(*args, **kw)
    return fn
    
#使用@performance,打印出函数调用的时间
import time

def performance(f):
    def fn(x):
        print'call',f.__name__+'()in',time.time()
        return f(x)
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y,range(1,n+1))
print(factorial(10))



'''
    1、python的decorator本质上就是一个高阶函数，接受一个函数作为参数，然后，返回一个新函数
    2、使用decorate用python提供的“@”语法，可以避免手动编写f =decorate代码。
    3、装饰器作用：
            #@log: 打印日志
            #@performance： 检测性能 
            #@transaction： 数据库事务  
            #@post('/register')： URL路由
    
