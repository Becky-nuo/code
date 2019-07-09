#MRO（）方法解析顺序

class A:
    def aa(self):
        print("aa")


    
    def aa(self):
        print("say AAA!")


class B:
    def bb(self):
        print("bb")


    def aa(self):
        print("say BBB!")



class C(B,A):
    def cc(self):
        print("cc")


c=C()
c.cc()
c.bb()
c.aa()
print(C.mro)  #打印类的层次结构
c.sasay() #解释器是寻找的方法是:“从走到右”的方式寻找。




'''
    1、MRO为方法解析顺序（从左到右）
    2、mro()方法获得MRO方法获得“类的层次结构”。
'''
