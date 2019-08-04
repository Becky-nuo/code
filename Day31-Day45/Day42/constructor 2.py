#普通方法和特殊的构造函数(继承)


class A:
    def hello(self): #类A定义了一个名为hello的方法，并被类B继承
        print("Hello, I'm A.")
class B(A):  #类B自己没有定义方法hello
    pass


a = A()
b = B()    #调用hello时，打印的是消息"Hello, I'm A."
print(a.hello())
print(b.hello())



#B可以重写方法hello
class B(A):
    def hello(self):
        print("Hello, I'm B.")


#修改定义后， b.hello()的结果将不同。
b = B()
print(b.hello())



#模拟鸟的进食
class Bird:
    def __init__(self):
        self.hungry = True
        def eat(self):
            if self.hungry:
                print('Aaaah ...')
                self.hungry = False
            else:
                print('No, thanks!')

'''这个类定义了所有鸟都具备的一种基本能力：进食'''

b = Bird()
print(b.eat())
print(b.eat())

'''鸟进食后就不再饥饿。下面来看子类SongBird，它新增了鸣叫功能'''
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
        def sing(self):
            print(self.sound)


sb = SongBird()
print(sb.sing())
print(sb.eat())



'''
    每个类都有一个或多个超类，并从它们那里继承行为。
    在子类中添加功能，一种基本方式是添加方法。然而，你可能想重写超类的某些方法，以定制继承而来的行为。


    重写是继承机制的一个重要方面，对构造函数来说尤其重要。
    构造函数用于初始化新建对象的状态，而对大多数子类来说，除超类的初始化代码外，还需要有自己的初始化代码。
    重写构造函数时，必须调用超类（继承的类）的构造函数，否则可能无法正确地初始化对象。


    SongBird是Bird的子类，继承了方法eat，但如果你尝试调用它，但出现了异常：

    在SongBird中重写了构造函数，但新的构造函数没有包含任何初始化属性hungry的代码，
要消除这种错误， SongBird的构造函数必须调用其超类（ Bird）的构造函数，以确保基本的初始化得以执行。

    
    有两种方法消除错误：调用未关联的超类构造函数，以及使用函数super。
    


'''






