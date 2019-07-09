#多重继承

class A:
    def aa(self):
        print("aa")


class B:
    def bb(self):
        print("bb")


class C(B,A):
    def cc(self):
        print("cc")


c=C()
c.cc()
c.bb()
c.aa()



'''
    1、python支持多重继承，一个子类可以有多个“直接父类”，也具备了"多个父类'的特点
    2、多重继承会造成“类的整体层次”搞得异常复杂，尽量避免使用。
'''
