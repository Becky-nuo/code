#作用域嵌套（Python函数可以嵌套，即可将一个函数放在另一个函数内）



def foo():
    def bar():
        print("Hello, world!")
        print(bar())


def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor



double = multiplier(2)
print(double(5))

triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))


'''
    像multiplyByFactor这样存储其所在作用域的函数称为闭包。
    通常，不能给外部作用域内的变量赋值，但如果一定要这样做，可使用关键字nonlocal。
    这个关键字的用法与global很像，让你能够给外部作用域（非全局作用域）内的变量赋值。


    嵌套通常用处不大，但有一个突出的用途：使用一个函数来创建另一个函数。
    一个函数位于另一个函数中，且外面的函数返回里面的函数。
    (每当外部函数被调用时，都将重新定义内部的函数，而变量factor的值也可能不同)
    也就是返回一个函数，而不是调用它。重要的是，返回的函数能够访问其定义所在的作用域。
    由于Python的嵌套作用域，可在内部函数中访问这个来自外部局部作用域（ multiplier）的变量。

'''
