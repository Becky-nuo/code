#python 中多重继承

class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin,Student):
    def __init__(self):
        super(BStudent,self).__init__()

class FTeacher(FootballMixin,Teacher):
    def __init__(self):
        super(FTeacher,self).__init__()


s = BStudent()
print(s.skill())

t = FTeacher()
print(t.skill())
        


'''
    1、除了一个父类继承外，pythob允许多个父类继承，称多重继承
    2、多重继承的目的是，从两种继承树中分别选择并继承除子类，以便组合功能使用。
    
'''

