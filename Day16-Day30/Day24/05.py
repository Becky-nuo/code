#python 中多态

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        def whoAmI(self):
            return 'I am Person ,my name is %s'% self.name

class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score
        def whoAmI(self):
            return 'I am a Student,my name is %s'% self.name

class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher,my name is %s'% self.namen


def who_am_i(x):
    print(x.whoAmI())

p = Person('Tim','Male')
s = Student('Bob','Male',99)
t = Teacher('Alice','Female','English')


print(who_am_i(p))
print(who_am_i(s))
print(who_am_i(t))



'''
    1、类具有继承关系，并且子类类型可以向上转型看做父类类型
    2、python是动态语言，所以，传递给函数who_am_i(x)的参数x不一定是person或person的子类型。
    3、动态语言调用实例方法，不检查类型，只有方法存在，参数正确，就可以调用。
    
'''
