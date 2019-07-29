#f分配参数


def add(x,y):
    return x +y


params = (1, 2) #假设有一个元组，其中包含两个要相加的数

add(*params)#这与前面执行的操作差不多是相反的：不是收集参数，而是分配参数。这是通过在调用函数（而不是定义函数）时使用运算符*实现的。


'''可用于参数列表的一部分，条件是这部分位于参数列表末尾(通过使用运算符**，可将字典中的值分配给关键字参数)。'''
params = {'name': 'Sir Robin', 'greeting': 'Well met'}
print(hello_3(**params)




#如果在定义和调用函数时都使用*或**，将只传递元组或字典。因此还不如不使用它们，还可省却些麻烦。

def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')
    args = {'name': 'Mr. Gumby', 'age': 42}
    print(with_stars(**args))
    print(without_stars(args))



#拆分运算符来传递参数(在调用超类的构造函数时特别有用)
def foo(x,y,z,m=0,n=0):
      print(x,y,z,m,n)

def call_foo(*arg,*kwds):
      print('Calling foo!')
      foo(*arg,**kwds)

      

'''
        对于函数with_stars，我在定义和调用它时都使用了星号，而对于函数without_stars，\
    我在定义和调用它时都没有使用，但这两种做法的效果相同。/
    因此，只有在定义函数（允许可变数量的参数） 或调用函数时（拆分字典或序列）使用，星号才能发挥作用。
    提示 使用这些拆分运算符来传递参数很有用，因为这样无需操心参数个数之类的问题。

'''
