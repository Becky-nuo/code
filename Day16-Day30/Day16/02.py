#方法的重写


class Person:  #父类


    def __init__(self,name,age):
        self.name=name
        self.__age=age   #私有



    def say_age(self):
        print("我的年龄:",self.__age)

        

    def say_introduce(self):
        print("我的名字是{0}".format(self.name))
        


class Student(Person):  #子类

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score=score


    def say_introduce(self):  #重写了父类的方法
        print("报告老师，我的名字是：{0}".format(self.name))


s=Student("小明",19,80)
s.say_age()
s.say_introduce()

'''
    1、成员继承：子类继承了父类除构造方法之外的所有成员
    2、方法重写：子类可以重新定义父类的方法，这样就会覆盖父类的方法，也称"重写"
'''
