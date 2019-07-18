#python 中__str__和__repr__


class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s,%s)' % (self.name,self.gender)
    __repr__ = __str__


p = Person('Bob','male')
print(p)




#给studeent类定义__str__和__repr__方法
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score


    def __str__(self):
        return '(Student:%s,%s,%s)'%(self.name,self.gender,self.score)
    __repr__ = __str__


s = Student('Bob','Male',85)
print(s)
