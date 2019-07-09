


#super()获得父类定义（代表父类的定义，而不是父类的对象）

class A:


    def say(self):
        print("A:",self)



class B(A):  #使用A类的方法

    def say(self):
        #A.say(self)  和super()效果一样（通过类名）
        super().say()
        print("B:",self)


B().say()  #调用B的方法
