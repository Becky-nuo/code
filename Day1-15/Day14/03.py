#静态方法

class Student:
    company = "abc"  #类属性

    
    @staticmethod
    def add(a,b):   #静态方法
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b
Student.add(20,30)





'''
    1、@classmethod必须位于方法上面一行
    2、调用静态方法格式：“类名。静态方法名（参数列表）”。
    3、静态方法中访问实例属性和实例方法会导致错误
    4、格式：
        @statimethod
        def 静态方法名（[形参列表]）:
            函数体
'''
