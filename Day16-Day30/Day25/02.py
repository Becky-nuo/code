#python 中获取对象信息

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student,my name is %s' % self.name

s = Student('Bob','Male',99)
print(type(s ))  #属性
print(dir(s))  #全部属性
print(s,'name')  #获取name属性

print(setattr(s,'name','Adam')) #设置新的name属性
print(s,'name') #新的name属性

print(s,'age') #获取age属性


'''
    1、dir()返回所有实例属性，返回的属性是字符串列表。
    
'''

