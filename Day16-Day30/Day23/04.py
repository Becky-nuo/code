#python 中类属性和实例属性名字冲突问题

class Person(object):
    address = 'Earth'
    def __init__(self,name):
        self.name= name


p1 = Person('Bob')
p2 = Person('Ailce')

print('Person.address = '+ Person.address)

p1.address = 'china'
print('p1.address = ' +p1.address) #p1的实例属性是：address(值是：china)


print('Person.address = '+ Person.address)
print('p1.address = ' + p2.address) #p2没有实例属性(address),但有类属性(address),使用返回‘Earth’




#在Person上把类属性count改为__count
class Person(object):

    __count = 0

    def __init__(self,name):
        self.name = name
        Person.__count+=1
        print(Person.__count)

a1 = Person('Bob')
a2 = Person('Ailce')

try:
    print(Person.__count)
except AttributeError:
    print('attributeeerror')


'''
    1、当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉队类属性的访问
    2、不可以在实例属性上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。
    
'''
