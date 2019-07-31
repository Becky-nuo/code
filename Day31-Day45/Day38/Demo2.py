#属性、函数各方法



class Class
def method(self)
print('I have a self!')
def function():
    print("I don't...")
    instance = Class()
    instance.method() I have a self!
    instance.method = function>>> instance.method() I don


class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)
print(bird = Bird())
print(bird.sing())
birdsong = bird.sing
print(birdsong())


c.name'Sir Lancelot'
c.name = 'Sir Gumby'
print(c.get_name())有些程序员认为这没问题，但有些程序员（如Smalltalk①之父）认为这违反了封装原则。



class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...")
        def accessible(self):
            print("The secret message is:")
            self.__inaccessible() #现在从外部不能访问__inaccessible，但在类中（如accessible中）依然可以使用它。


s = Secretive()
print(s.accessible())


print(Secretive._Secretive__inaccessible)

print(s._Secretive__inaccessible())
 


'''
    有没有参数self并不取决于是否以刚才使用的方式（如instance.method）调用方法。实际上，完全可以让另一个变量指向同一个

    外部完全隐藏对象的状态（即不能从外部访问它们）。

    能直接访问ClosedObject（对象c所属的类）的属性name，就不需要创建方法setName和getName了。

    方法（更准确地说是关联的方法）将其第一个参数关联到它所属的实例，因此无需提供这个参数。
无疑可以将属性关联到一个普通函数，但这样就没有特殊的self参数了。

    方法set_name中。但如果直接设置c.name(将属性定义为私有,私有属性不能从对象外部访问，
而只能通过存取器方法（如get_name和set_name）来访问。)

    方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可性、
函数和方法实际上，方法和函数的区别表现在前一节提到的参数self上。

    在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头加上一个下划线和类名。

    from module import *不会导入以一个下划线打头的名称。
    
'''
