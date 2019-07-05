#lambda表达式和匿名函数

f = lambda a,b,c:a+b+c #冒号前面是形参，后面为表达式

def test01(a,b,c):
    return(a*b*c)

print(f(2,3,4))


g=[lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g[0](6),g[1](7),g[2](8))  #相当于赋值


h=[test01,test01]   #函数也是对象
print(h[0](6,7,8))

'''
    1、lambda表达式可以用来声明匿名函数。
    2、lambda函数是一种简单，在同一行中定义函数的方法。
    3、lambda函数实际生成一个函数对象。
    4、lambda表达式只允许包含一个表达式，不能包含复杂语句，表达式的计算结果是函数的返回值。
    5、语法：
            lambda arg1,arg2,arg3...:<表达式>
        arg1/arg2/arg3为函数的参数，<表达式>相当于函数体,运算结果是表达式的结果。
'''
