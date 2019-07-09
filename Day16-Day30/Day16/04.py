#重写object的__str__()

class Person:    #默认继承object类
    def __init__(self,name):
        self.name=name



    def __str__(self):
        return '名字是：{0}'.format(self.name)


p=Person("小明")
print(p)


'''
    1、__init__()方法，用于返回一个对于“对象的描述”。
    2、内置函数str()经常用于print()方法，帮助查看对象信息。
    3、__str()__可以重写
'''
