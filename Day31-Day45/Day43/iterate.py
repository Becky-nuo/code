#迭代器协议


#斐波那契数列
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


#创建一个对象

fibs = Fibs()

'''在for循环中使用这个对象，找出第一个大于1000的斐波那契数'''
for f in fibs:
    if f > 1000:
        print(f)
        break  #停止执行



'''

    迭代器就是重复多次。

    方法__iter__返回一个迭代器，它是包含方法__iter__的对象，调用这个方法可以不提供任何参数。

    用方法__next__时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，应引发StopIteration异常。
    
    内置的便利函数next，在这种情况下， next(it)与it.__next__()等效。
    
    在Python 3中，迭代器协议有细微的变化。在以前的迭代器协议中，要求迭代器对象包含方法next而不是__next__。

    计算值的函数，想逐个获取值，不是使用列表一次性获取，这因为如果有很多值，列表可能占用太多的内存。
    
    迭代器的方法__iter__，在for循环中使用这个对象，在迭代器中实现方法__iter__（并像刚才那样让它返回self），
这样迭代器就可直接用于for循环中。

    方法__iter__的对象是可迭代的，方法__next__的对象是迭代器。

    

'''
