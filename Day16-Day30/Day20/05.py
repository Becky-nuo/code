#python中匿名函数



def is_not_empty(s):
    return s and len(s.strip()) > 0

print(list(filter(is_not_empty,['test',None,'','str','  ','END'])))





import random

li = [random.randint(1,10)for i in range(10)]
print(li)
print(sorted(li,key=lambda x:1 if x % 2 ==0 else 0))
print(sorted(li,key=lambda x: x%2==0))


'''
    1、高阶函数可以接收函数做参考，有些时候，我们不需要显示定义函数，直接传入匿名函数更方便。
    2、匿名函数只能有一个表达式，不写return,返回值就是该表达式的结果。
    3、在python中，对匿名函数提供了有限的支持
    4、使用匿名函数可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码。
    5、关键字lambda表示匿名函数，冒号前面的x表示函数参数。

'''
