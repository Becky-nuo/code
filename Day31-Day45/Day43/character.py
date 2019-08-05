#特性(用于获取或设置属性)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width,self.height = size

    def get_size(self):
        return self.width, self.height




#使用类
r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size)


r.size = 150, 100
print(r.width)




'''
    如果访问给定属性时必须采取特定的措施，那么像这样封装状态变量（属性）很重要。

    get_size和set_size是假想属性size的存取方法，这个属性是一个由width和height组成的元组。
            （可随便将这个属性替换为更有趣的属性，如矩形的面积或其对角线长度）

    使用类时，无需关心它是如何实现的（封装）。

    想修改实现时，让size成为真正的属性，而width和height是动态计算出来的，
就需要提供用于访问width和height的存取方法，使用这个类的程序也必须重写。

    让客户端代码（使用你所编写代码的代码）能够以同样的方式对待所有的属性。

    Python能够替你隐藏存取方法，让所有的属性看起来都一样。

    有大量简单的属性，这样做就不现实（而且有点傻），因为将需要编写大量这样的存取方法，
除了获取或设置属性外什么都不做。

    在Python中，实际上有两种创建特定的机制。



'''
