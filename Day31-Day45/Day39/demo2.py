
#抽象基类（有比手工检查各个方法更好的选择）



from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod  #装饰器
    def talk(self):
        pass

print(Talker())



'''假设像下面这样从它派生出一个子类：'''

class Knigget(Talker):
    pass



class Knigget(Talker):
    def talk(self):
        print("Ni!")


k = Knigget()
print(isinstance(k, Talker))
print(k.talk)
class Herring:
    def talk(self):
        print("Blub.")


h = Herring()
print(isinstance(h, Talker))  #不是Talker对象。



print(Talker.register(Herring))
print(isinstance(h, Talker))
print(issubclass(Herring, Talker))


class Clam:
    pass

print(Talker.register(Clam))
print(issubclass(Clam, Talker))
c = Clam()
print(isinstance(c, Talker))
print(c.talk)



'''
    即假设所有对象都能完成其工作，同时偶尔使用hasattr来检查所需的方法是否存在。
    Python通过引入模块abc提供了官方解决方案。这个模块为所谓的抽象基类提供了支持。



    这里的要点是你使用@abstractmethod来将方法标记为抽象的——在子类中必须实现的方法。
    抽象类（即包含抽象方法的类）最重要的特征是不能实例化。


    由于没有重写方法talk，因此这个类也是抽象的，不能实例化。
    抽象基类的主要用途，只有在在实例化它没有任何问题的情形下使用isinstance才是妥当的

    将isinstance返回True视为一种意图表达。
    标准库（如模块collections.abc）提供了多个很有用的抽象类
'''
