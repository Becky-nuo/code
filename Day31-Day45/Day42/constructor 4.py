#函数 super（只适用于新式类）



class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)


'''新式版本与旧式版本等效：'''

sb = SongBird()
print()sb.sing()
print(sb.eat())
print(sb.eat())






'''
    调用这个函数时，将当前类和当前实例作为参数。
    对其返回的对象调用方法时，调用的将是超类（而不是当前类） 的方法。

    通常那样（也就是像调用关联的方法那样）调用方法__init__。

    在Python 3中调用函数super时，可不提供任何参数（通常也应该这样做）。


    相比于直接对超类调用未关联方法，使用函数super更直观。

    函数super有多个超类，也只需调用函数super一次（条件是所有超类的构造函数也使用函数super）。

    函数super返回的是一个super对象，这个对象将负责为你执行方法解析。

    

'''
