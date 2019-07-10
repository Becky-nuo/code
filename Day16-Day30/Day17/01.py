#多态

class Man:
    def eat(self):
        print("饿了")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")



class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")


class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")



def manEat(m):
    if isinstance(m,Man):
        m.eat()         #多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print("不能吃饭")


manEat(Chinese())
manEat(English())


'''
    1、多态指同一个方法调用由于对象不同可能会产生不同的行为。
    2、多态是方法的多态，属性没有多态。
    3、多态的存在有两个必要条件:继承、方法重写。
'''
    
    
