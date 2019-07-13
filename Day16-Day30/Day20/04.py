#python中闭包

def g():
    print 'g()...'

def f():
    print 'f()...'
    return g

#将g的定义移入函数f内部，防止其他代码调用g
def f():
    print'f()...'

    def g():
        print'g()...'
    return g


    
#一次性返回3个函数，分别计算1*1，2*2，3*3'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(count)



 
'''
    1、内层函数引用了外层函数的局部变量（参数也算变量），然后返回内层函数的情况，成为闭包
    2、闭包特点：返回函数还引用了外部函数的布局变量
    3、在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问

'''
