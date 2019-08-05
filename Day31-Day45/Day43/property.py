#函数property(将存取方法作为参数，获取方法在前，设置方法在后)

#创建一个特性
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width,self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size,set_size) #把名称size关联到特性上



r = Rectangle()
r.width = 10
r.height = 5
print(r.size)


r.size = 150, 100
print(r.width)





'''
    如果特性的行为怪异，务必确保你使用的是新式类（通过直接或间接地继承object或直接设置__metaclass__）。

    特性的获取方法依然正常，但设置方法可能不正常（是否如此取决于使用的Python版本）。

    调用函数property时，还可不指定参数、指定一个参数、指定三个参数或指定四个参数;
如果没有指定任何参数，创建的特性将既不可读也不可写。如果只指定一个参数（获取方法），创建的特性将是只读的;
第三个参数是可选的，指定用于删除属性的方法（这个方法不接受任何参数）;第四个参数也是可选的，指定一个文档字符串。

    创建一个只可写且带文档字符串的特性，可使用它们作为关键字参数来实现。

    对于新式类，应使用特性而不是存取方法。


'''
