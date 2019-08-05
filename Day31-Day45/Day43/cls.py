#静态方法和类方法

讨论旧的特性实现方式之前，先来说说另外两种实现方式类似于新式特性的功能。
静态方法和类方法是这样创建的：将它们分别包装在staticmethod和classmethod类的对象中。
静态方法的定义中没有参数self，可直接通过类来调用。
类方法的定义中包含类似于self的参数，通常被命名为cls。
对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。下面是一个简单的示例：

class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)
    
    def cmeth(cls):
        print('This is a class method of', cls)
    cmeth = classmethod(cmeth）


class MyClass:


    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethoddef cmeth(cls):   #定义方法后，不需要实例化类
        print('This is a class method of', cls)



print(MyClass.smeth())
print(MyClass.cmeth())





'''
    静态方法和类方法的创建：将它们分别包装在staticmethod和classmethod类的对象中。
    静态方法的定义中没有参数self，可直接通过类来调用。
    类方法的定义中包含类似于self的参数，通常被命名为cls。
    类方法，通过对象直接调用，但参数cls将自动关联到类。


    装饰器可用于包装任何可调用的对象，并且可用于方法和函数。
    指定一个或多个装饰器，为此可在方法（或函数）前面使用运算符@列出这些装饰器。
        （指定了多个装饰器时，应用的顺序与列出的顺序相反）



'''
