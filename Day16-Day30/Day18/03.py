#模块导入(from...import导入)




def add(a,b):
    return a+b


def minus():
    return a-b


class MyNum():
    def print123(self):
        print(123)





'''
    1、基本语法格式：
            from 模块名 import 成员1,成员2,....   （导入模块中的成员）
            from 模块名 import *   (导入一个模块中的所有成员)

    2、import语句和from...import语句的区别：
        a、import导入的是模块。from...import导入的是模块中的一个函数/一个类。
        b、进行类别的话:import导入的是文件，使用“该”下的内容，必须前面加“文件名称”。/
     from...import导入的是文件下的“内容”直接使用这些内容即可，/
     前面再也不需要加“文件名称”了。   
'''
