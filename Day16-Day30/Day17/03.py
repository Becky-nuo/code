#特殊属性（python对象中包含的下划线有开始和结束的属性）

class A:
    def aa(self):
        print("aa")


    
    def say(self):
        print("say AAA!")


class B:
    def bb(self):
        print("bb")


    def say(self):
        print("say BBB!")



class C(B,A):
    def __init__(self,nn):
        self.nn=nn
    
    def cc(self):
        print("cc")


c = C(3)
print(C.mro())    #打印类的层次结构
c.say()           #解释器是寻找的方法是:“从走到右”的方式寻找。

print(dir(c))
print(c.__dict__)  #obj.__dict__,对象的属性字典
print(c.__class__)    #obj.__class__,对象所属的类
print(C.__bases__)    #class.__bases,类的基类元组（多继承）
print(C.__base__)    #class.__base__,类的基类
print(C.mro())      #class.__mro__,类层次结构
print(A.__subclasses__())  #class.__subclasses__(),子类列表
