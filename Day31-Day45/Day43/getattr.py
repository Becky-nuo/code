#__getattr__、 __setattr__方法（拦截对对象属性的所有访问企图、在旧式类中实现特性）



#使用魔法方法：
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self. __dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError


'''

魔法方法：（在旧式类中，只需使用后面三个）
    __getattribute__(self, name)：在属性被访问时自动调用（只适用于新式类）。
    __getattr__(self, name)：在属性被访问而对象没有这样的属性时自动调用。
    __setattr__(self, name, value)：试图给属性赋值时自动调用。
    __delattr__(self, name)：试图删除属性时自动调用。

    相比函数property，这些魔法方法使用起来要棘手些（从某种程度上说，效率也更低），
但它们很有用，因为你可在这些方法中编写处理多个特性的代码。


    编写方法__setattr__时需要避开无限循环陷阱，编写__getattribute__也是一样。
由于它拦截对所有属性的访问（在新式类中），因此将拦截对__dict__的访问！
在 __getattribute__中访问当前实例的属性时，唯一安全的方式是使用超类的方法__getattribute__（使用super)




    即便涉及的属性不是size，也将调用方法__setattr__。因此这个方法必须考虑如下两种情形：
如果涉及的属性为size，就执行与以前一样的操作；否则就使用魔法属性__dict__。
__dict__属性是一个字典，其中包含所有的实例属性。之所以使用它而不是执行常规属性赋值，
是因为旨在避免再次调用__setattr__，进而导致无限循环。

    没有找到指定的属性时，才会调用方法__getattr__。这意味着如果指定的名称不是size，
这个方法将引发AttributeError异常。这在要让类能够正确地支持hasattr和getattr等内置函数时很重要。
如果指定的名称为size，就使用前一个实现中的表达式。




'''
