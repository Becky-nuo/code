#python 中判断类型

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self,name,gendern,score):
        super(Student,self).__init__(name,gender)
        self.score = score

class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course

t = Teacher('Ailce','Female','English')
 
print(isinstance(t,Person))
print(isinstance(t,Student))
print(isinstance(t,Teacher))
print(isinstance(t,object))


'''
1、函数isinstance()可以判断一个变量的类型
2、在继承链上，一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法
3、在继承链上，一个实例可以看成它本身的类型，也可以看成它父类的类型

'''
