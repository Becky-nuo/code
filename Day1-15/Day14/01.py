#类属性

class Student:
    company = "abc"  #类属性
    count = 0   #类属性


    def __int__(self,name,score):
        self.name = name   #实例属性
        self.score = score
        Student.count = Student.count+1


    def say_score(self):   #实例方法
        print("我的公司是: ",Student.company)
        print(self.name,'的分数是:',self.score)



s1 = Student('小明',80)   #s1是实例对象，自动调用__init__()方法
s1.say_score()
print('一共创建{0}个Student对象'.format(Student.count))



'''
    1、类属性是从属于“类对象”的属性，也称为“类对象”
    2、类属性从属于类对象，可以被所有实例对象共享
    3、类属性的定义方式：
            class 类名：
                类变量名 = 初始值
'''
