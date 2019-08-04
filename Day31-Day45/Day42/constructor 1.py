
#构造函数(对象创建后自动调用)


#普通版
f = Person()
f.init()



#魔法版

f = Person()
class Person:
    def __init__(self):
        self.somevar = 42
f = person()
print(f.somevar)


#给构造函数添加几个参数
class Person:
    def __init__(self, value=42):
        self.somevar = value



f = Person('This is a constructor')
print(f.somevar)





'''

    构造函数（ constructor），就是示例中使用的初始化方法，只是命名为__init__。

    在Python中，创建构造函数很容易，只需将方法init的名称从普通的init改为魔法版__init__即可。

    由于参数是可选的，你可以当什么事都没发生。

    在所有的Python魔法方法中， __init__绝对是你用得最多的。

    Python提供了魔法方法__del__，也称作析构函数（ destructor），
这个方法在对象被销毁（作为垃圾被收集）前被调用。

'''

