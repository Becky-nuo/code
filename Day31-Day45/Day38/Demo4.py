#指定超类(子类扩展了超类的定义)



class Filter:  #在class语句中的类名后加上超类名，并将其用圆括号括起。
    def init(self):
        self.blocked = []
        def filter(self, sequence):
            return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter是Filter的子类
    def init(self): # 重写超类Filter的方法init
        self.blocked = ['SPAM']



f = Filter()  #Filter是一个过滤序列的通用类,但它不会过滤掉任何东西。
f.init()
print(f.filter([1, 2, 3]))



s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))




'''
    Filter类的用途在于可用作其他类（如将'SPAM'从序列中过滤掉的SPAMFilter类）的基类（超类）。


    注意SPAMFilter类的定义中有两个要点:
                        提供新定义的方式重写了Filter类中方法init的定义。
                        直接从Filter类继承了方法filter的定义，因此无需重新编写其定义。

    第二点说明了继承很有用的原因：
            可以创建大量不同的过滤器类，它们都从Filter类派生而来，
            并且都使用已编写好的方法filter。这就是懒惰的好处。
            
'''
