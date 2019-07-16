#python 中定义实例方法

class Person(object):
    def __init__(self,name):
        self.__name = name

    def get__name(self):
        return self.__name
    
p1 = Person('Bob')
print(p1.get__name()) #self不需要显示传入




#给Person，增加一个私有属性__score
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score
    def get__grade(self):
        if self.__score>=90:
            return 'A-优秀'
        elif self.__score>=60:
            return 'B-及格'
        else:
            return 'C-不及格'
        
a1 = Person('Bob',90)
a2 = Person('Ailce',30)
a3 = Person('Tim',70)
        
print(a1.get__grade())
print(a2.get__grade())
print(a3.get__grade())



'''
    1、一个实例的私有属性就是以__开头的属性，无法被外部访问
    2、私有属性无法被外部访问，但是，从类的内部是可以访问的，定义实例的属性和实例方法。
    3、实例方法就是在类中定义函数，它的第一个参数永远是self,指向调用该方法的实例本身。
    4、在实例方法内部 可以访问所有实例属性，如果外部需要访问私有属性，可以通过方法调用获得。
    
'''
