#object根类_dir()

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age



    def say_age(self):
        print(self.name,"的年龄是:",self.age)


obj=object()
print(dir(obj))


s2=Person("小明",19)
print(dir(s2))


'''
    1、person 对象增加了六属性：
    _dir_  _module_  _weakref_  age   name   say_age
    2、object的所有属性，Person类作为object的子类，显然包含了所有属性。
    3、age、name、say_age，发现say_age虽然是方法，实际上也是属性，只不过，属性的类型是“method”而已
            age<class 'int'>
            name<class 'str'>
            say_age<class 'method'> 
'''
