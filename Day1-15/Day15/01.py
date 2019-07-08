#方法没有重载

class Person:

    def say_hi(self):   #失效
        print("hello")


    def say_hi(self,name):
        print("{0},hello".format(name))


p1 = Person()


#p1.say_hi()    不带参，报错
p1.say_hi("小明")


''' 1、python中没有方法的重载，定义多个同名方法，只有最后一个有效
    2、方法的参数没有类型（调用时确定参数的类型），参数的数量也可以由可变参数控制。
    3、
'''
