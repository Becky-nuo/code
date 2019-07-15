#python中创建实例属性

class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1,p2,p3]
L2 = sorted(L1,key=lambda x:x.name) #自然排序返回list列表，可以接收多个参数

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)


'''
    1、由于python是动态语言，对每一个实例都可以直接给他们的属性赋值
    2、实例的属性可以像普通变量一样进行操作
    
'''
