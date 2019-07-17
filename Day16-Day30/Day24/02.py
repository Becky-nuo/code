#python 中定义类方法

class Person(object):
    count = 0
    
    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self,name):
        self.name = name
        Person.count =Person.count + 1


print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
    

#将类属性count改为__count,则外部无法读取__score
class Person(object):
    count =  0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self,name):
        self.name = name
        Person.__count = Person.__count + 1

print(Person.how_many())
a1 = Person('Bob')
print(Person.how_many())
    
'''
    1、和类属性一样，方法也有实例方法和类方法。
    2、在class中定义的全部是实例方法，实例方法第一个参数self是实例本身。
    3、类方法的第一个参数将传入类本身，通常将参数命名为cls。
    4、在类上调用，而非实例上调用，类方法无法获得任何实例变量，只能获得类的引用
    
'''
