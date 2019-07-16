#python中创建类属性

class Person(object):
    address = 'Earth'
    def __init__(self,name):
        self.name = name

print(Person.address) 


p1 = Person('Bob')
p2 = Person('Alice')
print(p1.address)   #绑定在一个实例上的属性不会影响其他实例
print(p2.address)



#给Person创建一个属性，创建一个实例，count属性就加1
class Person(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count+=1


a1 = Person('Bob')
print(Person.count)

a2 = Person('Aile')
print(Person.count)

a3 = Person('Tim')
print(Person.count)


'''
    1、类是模板，而实例则是根据类创建的对象
    2、实例属性每一个实例各自拥有，互相独立。而类属性有且只有一份
    3、类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问’
    4、python是动态语言，类属性也是可以动态添加和修改的
'''
