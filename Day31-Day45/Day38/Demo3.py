#类的命名空间

类的命名空间下面两条语句大致等价：

def foo(x):
    return x * x
foo = lambda x: x * x



class C:   #成员变量（属性）
    print('Class C being defined...')

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1
        m1 = MemberCounter()
        m1.init()  #init初始化实例（初始化过程自动化）
        print(MemberCounter.members)
        m2 = MemberCounter()
        m2.init()
        MemberCounter.members


print(m1.members)
print(m2.members)


#给属性members赋值
m1.members = 'Two'
print(m1.members)
print(m2.members)

#新值被写入m1的一个属性中，这个属性遮住了类级变量。


'''
    创建一个返回参数平方的函数，并将这个函数关联到变量foo,
可以在全局（模块）作用域内定义名称foo，也可以在函数或方法内定义。


    以一个和两个下划线打头相当于两种不同的私有程度的代码都是在一个特殊的
命名空间（ 类的命名空间）内执行的，而类的所有成员都可访问这个命名空间。

    类作用域内定义了一个变量，所有的成员（实例）都可访问它，这里使用它来计算类实例的数量。

'''
