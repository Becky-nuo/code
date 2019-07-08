#私有属性和私有方法

class Employee:


    def __init__(self,name,age):
        self.name = name
        self.__age = age   #私有属性


    def __f1(self):      #私有方法
        print("abcdefgh")

        


e = Employee("小明",19)


print(e,name)
#print(e,age)
print(e._Employee__age)
print(dir(e))
e._Employee__f1()


'''
    1、通常我们约定，两个下划线开头的属性是私有的（private),其它为公共的（public）
    2、类内部可以访问私有属性（方法）
    3、类外部不能直接访问私有属性（方法）
    4、类外部可以通过“_类名_私有属性（方法）名”访问私有属性
    5、方法本质上也是属性！只不过是可以通过（）执行而已
    
'''
