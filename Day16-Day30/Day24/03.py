#python中继承一个类

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender) #初始化父类
        self.score = score




#编写一个Teacher类，继承Person

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course


t = Teacher('Ailce','Female','English')
print(t.name)
print(t.course)


