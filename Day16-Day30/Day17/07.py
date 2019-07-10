#单列模式


class MySingleton:


    __obj = None       #类属性
    __init_flag = True


    def __new__(cls,*args,**kwargs):
        if cls.__obj ==None:
            cls.__obj =object.__new__(cls)


            return cls.__obj


    def __init__(self,name):
        if MySingleton.__init_flag:
            print("init....")
            self.name = name
            MySingleton.__init_flag = False


a = MySingleton("aa")
b = MySingleton("bb")
print(a)
print(b)
c = MySingleton("cc")
print(c)




'''
    1、单列模式的核心作用是确保一个类只有一个实例，并且提供一个访问该实例的全属访问点
    2、单列模式只生产一个实例对象，减少了对系统资源的开销（当一个对象的产生需要比较多的资源）
    
'''
