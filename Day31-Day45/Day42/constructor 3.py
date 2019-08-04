#调用未关联的超类构造函数(用于解决历史遗留问题)


#在SongBird类中，只添加了一行，其中包含代码Bird.__init__(self)。
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBird()
print(sb.sing())
print(sb.eat())
print(sb.eat())




'''
关联方法和未关联方法之间的差别:

    对实例调用方法时，方法的参数self将自动关联到实例,称为关联的方法。

    通过类调用方法（如Bird.__init__），就没有实例与其相关联，
可随便设置参数self。这样的方法称为未关联的。



    未关联方法的self参数设置为当前实例，将使用超类的构造函数来初始化SongBird对象。

'''
