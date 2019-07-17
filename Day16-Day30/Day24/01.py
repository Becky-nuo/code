#python 中方法也是属性

class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        return 'A'

p1 = Person('Bob',90)
print(p1.get_grade)
print(p1.get_grade())



#属性可以是普通的值对象
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

a1 = Person('Bob',90)
print(p1.get_grade)
print(p1.get_grade())

'''
    1、方法也是一个属性，所以，它可以动态地添加到实例上，只需要把一个函数变为一个方法。

'''
