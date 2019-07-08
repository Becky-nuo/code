#方法的动态性

class Person:

    def f1(self):
        print("hello")


def f2(s):
    print("{0}在上课".format(s))


def f3(s):
    print("abcdefg")



Person.f2 = f2
p=person()
p.f1()
p.f2()    #Person.f2(P)

Person.f2 = f3
p.f3()



'''
    1、python是动态语言，我们可以死动态的为类添加新的方法，或者动态的修改类的已有的方法
'''
