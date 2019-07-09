#继承的基本使用


class Person:  #父类


    def __init__(self,name,age):
        self.name=name
        self.age=age



    def say_age(self):
        print("年龄，年龄，年龄")



class Student(Person):  #子类

    def __init__(self,name,age,score):
        Person.__init__(self,name,age) #必须显示的调用父类初始化方法，不然解释器不会去调用
        self.score=score


#Student-->Person-->object类
        
print(Student.mro())

s=Student("小明",19,70)
s.say_age()
print(s.name)


'''
    1、如果再类定义中没有指定父类，则默认父类是object类。object是所有类的父类（__new__()）
    2、定义子类时，必须在其构造函数中调用父类的构造函数，格式（父类名.__init__(self,参数列表)）
    3、一个子类可以继承多个父类
    4、语法格式：
        class 子类类名（父类1[父类2,,....]）:
'''
