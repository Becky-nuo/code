#递归式生成器（使用两个for循环来实现）


#递归
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested



print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))



#检查后的生成器
def flatten(nested):
    try:      # 不迭代类似于字符串的对象tr
        try:nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested



list(flatten(['foo', ['bar', ['baz']]]))





'''
    处理任意层嵌套的列表来表示树结构（也可以使用特定的树类，但策略是相同的）。

    对于每层嵌套，都需要一个for循环，但由于不知道有多少层嵌套，你必须修改解决方案，使其更灵活。



    调用flatten时，有两种可能性（处理递归时都如此）： 基线条件和递归条件。

    在基线条件下，要求这个函数展开单个元素（如一个数）。
    要展开一个列表（或其他任何可迭代对象）时，你需要做遍历所有的子列表（其中有些可能并不是列表）
并对调用flatten，然后使用另一个for循环生成展开后的子列表中的所有元素。


    如果nested是字符串或类似于字符串的对象，它就属于序列，因此不会引发TypeError异常，可你并不想对其进行迭代


    在函数flatten中，不应该对类似于字符串的对象进行迭代，主要原因有两个:
        1、将类似于字符串的对象视为原子值，而不是应该展开的序列。
        2、对字符串的对象进行迭代会导致无穷递归，因为字符串的第一个元素是一个长度为1的字符串，
而长度为1的字符串的第一个元素是字符串本身。

    检查对象时，要检查是否类似于字符串，最简单、最快捷的方式是，尝试将对象与一个字符串拼接起来，
并检查这是否会引发TypeError异常。

    内部try语句中的else子句将引发TypeError异常，这样将在外部的excpet子句中原封不动地生成类似于字符串的对象。


    没有检查nested是否是字符串，而只是检查其行为是否类似于字符串，即能否与字符串拼接。
        1、一种更自然的替代方案是，使用isinstance以及字符串和类似于字符串的对象的一些抽象超类，但遗憾的是没有这样的标准类。
        2、即便是对UserString来说，也无法检查其类型是否为str。






'''
