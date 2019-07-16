#python 中访问限制

class Person(object):
    def __init__(self,name):
        self.name = name
        self.__title = 'Mr'
        self.__job = 'Student' #__job不能直接被外部访问

P = Person('Bob')
print(P.name)




#用Person类的__init__方法中添加name和score参数
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

A = Person('Bob',80)
print(A.name)

try:
    print(A.__score)
except AttributeError:
    print(A.name)
    print('attribute error')


'''
    1、python对属性权限的控制是通过属性名来实现的（双下划线开头__）

'''
