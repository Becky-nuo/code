#创建自定义类

#创建自定义类终于要创建自定义类！

__metaclass__ = type   # 如果你使用的是Python 2，请包含这行代码

class Person:
    def set_name(self, name):
        self.name = name
        def get_name(self):
            return self.namedef greet(self):
                print("Hello, world! I'm {}.".format(self.name))


foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')
print(foo.greet())
print(bar.greet())  #对foo调用set_name和greet时， foo都会作为第一个参数自动传递给它们。


foo.name'Luke Skywalker'
bar.name = 'Yoda'
bar.greet()Hello, world! I'm Yoda.

提示 如果foo是一个Person实例，可将foo.greet()视为Person.greet(foo)的简写，但后者的多态性更低。



'''
    旧式类和新式类是有差别的(Python 3之前，默认创建的是旧式类)
    所有的方法都无法访问对象本身——要操作的属性所属的对象。

'''
