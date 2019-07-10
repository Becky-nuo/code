#组合

class A1:

    def say_a1(self):
        print("a1,a1,a1")


class B1(A1):
    pass

b1 = B1()
b1.say_a1()



#同样的效果，使用组合实现代码的复用
class A2:
    def say_a2(self):
        print("a2,a2,a2")


class B2:
    def __init__(self,a):
        self.a = a



a2 = A2()
b2 = B2(a2)
b2.a.say_a2()
    

'''
    1、"is-a"关系，可以使用“继承”，从而实现子类拥有的父类的方法和属性
    2、"has-a"关系，可以使用“组合”，也能实现一个类拥有另一个类的方法和属性
    
'''
