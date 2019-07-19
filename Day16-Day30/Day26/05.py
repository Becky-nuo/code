#python 中__call__

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


    def __call__(self,friend):
        print('my name is %s...' % self.name)
        print('my friend is %s...' % friend)


p = Person('Bob','male')
print(p('Tim'))





class Fib(object):

    def __call__(self,num):
        a = 0
        b = 1
        c = []

        for i in range(num):
            c.append(a)
            a,b = b,a+b

        return c

f = Fib()
print(f(10))


'''
    1、所有函数都是可调用对象
    2、一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
    3、在python中，函数也是对象，对象和函数的区别不显著
    
'''
