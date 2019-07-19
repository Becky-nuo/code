#python中 __slots__

class Person(object):
    __slots__ = ('name','gender')

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


class Student(Person):

    __slots__ =('score')  #限制当前类所能拥有的属性（节省内存）

    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score


s = Student('Bob','male',59)
s.name = 'Tim'
s.score = 99
print(s.score)


'''
    1、python是动态语言，任何实例运行期都可以动态地添加属性
    
'''
