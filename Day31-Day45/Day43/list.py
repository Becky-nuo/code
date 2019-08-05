#基本的序列



#一个带访问计数器的列表
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
            self.counter += 1
            return super(CounterList, self).__getitem__(index)


cl = CounterList(range(10))
print(cl.reverse())
print(cl)


del cl[3:6]
print(cl)
print(cl.counter)
print(cl[4] + cl[2])
print(cl.counter)




'''
    类深深地依赖于其超类（ list）的行为。
    CounterList没有重写的方法（如append、 extend、 index等）都可直接使用。

    在两个被重写的方法中，使用super来调用超类的相应方法，并添加了必要的行为：
初始化属性counter（在__init__中）和更新属性counter（在__getitem__中）。

     重写__getitem__并不能保证一定会捕捉用户的访问操作，因为还有其他访问列表内容的方式。

     在标准库中，模块collections提供了抽象和具体的基类，但你也可以继承内置类型。

'''
