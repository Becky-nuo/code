#python 之定义类并创建实例

class Person(object):
    pass

xiaoming = Person()
xiaohong = Person()


print(xiaoming)
print(xiaohong)
print(xiaoming==xiaohong)  #打印的是False，说明它们的内存中的地址不一样


'''
    1、在python中，类通过class关键定义
    2、在python中，类名以大写字母开头，紧接着是（object）,表示该类从哪继承下来的
    
'''
