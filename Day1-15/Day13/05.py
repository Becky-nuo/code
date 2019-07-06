#类对象

class Student:
    pass    #空语句

print(type(Student))  
print(id(Student))  #地址

Stu2 = Student  #创建了一个新的类对象
s1 = Stu2()
print(s1)




'''
    1、当解释器执行class语句时，会创建一个类对象
    2、当我们赋值给新变量的时候，也可以实现相关的调用，创建了一个“类对象”
    3、pass为空语句，表示什么都没做，只是作为一个占位符存在/
    （当你写代码遇到暂时不知道往方法或者类中加入什么时，可以先用pass占位，后期补上）
'''
