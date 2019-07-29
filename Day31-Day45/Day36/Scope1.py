
#作用域


#返回不可见的字典（命名空间或作用域）

x = 1
scope = vars()
scope['x']
scope['x'] += 1


def foo():   #函数foo修改（重新关联）了变量x，但当你最终查看时，它根本没变
    x = 42    #内部作用域（局部命名空间）中执行的，不影响外部（ 全局）作用域内的x）。
    x = 1
    foo()
    print(x)


def output(x):
    print(x)
    x = 1
    y = 2
    print(output(y))


def combine(parameter):
    print(parameter + external)
    external = 'berry'
    print(combine('shrub'))


'''
    不应修改vars返回的字典，因为根据Python官方文档的说法，这样做的结果是不确定的。换而言之，可能得不到你想要的结果。
    “看不见的字典”称为命名空间或作用域,除全局作用域外，每个函数调用都将创建一个。


    变量是可将其视为指向值的名称。因此，执行赋值语句x = 1后，名称x指向值1。
    这几乎与使用字典时一样（字典中的键指向值），只是你使用的是“看不见”的字典。，
