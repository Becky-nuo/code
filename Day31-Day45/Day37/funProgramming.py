#函数式编程（赋予变量，作为参数进行传递，从函数返回）



list(map(str, range(10))) # 与[str(i) for i in range(10)]等价


def func(x):  #可以使用filter根据布尔函数的返回值来对元素进行过滤。
    return x.isalnum()

print(seq = ["foo", "x41", "?!", "***"])
print(list(filter(func, seq)))

print([x for x in seq if x.isalnum()]  #如果转而使用列表推导，就无需创建前述自定义函数。

print( filter(lambda x: x.isalnum(), seq))


numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
print(reduce(lambda x, y: x + y, numbers))




'''
    Python提供了一些有助于进行这种函数式编程的函数： map、 filter和reduce。
在较新的Python版本中，函数map和filter的用途并不大，应该使用列表推导来替代它们。
可以使用map将序列的所有元素传递给函数。

    Python提供了一种名为lambda表达式①的功能，让你能够创建内嵌的简单函数（主要供map、 filter和reduce使用）。

    要使用列表推导来替换函数reduce不那么容易，而这个函数提供的功能即便能用到，也用得不多。
    使用指定的函数将序列的前两个元素合二为一，再将结果与第3个元素合二为一，依此类推，
直到处理完整个序列并得到一个结果。。例如，如果你要将序列中的所有数相加，可结合使用reduce和lambda x, y: x+y
'''

      
