#多个超类（复数形式的__bases__）



#创建几个类
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:def talk(self):
    print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):  #子类TalkingCalculator,它所有的行为都是从超类那里继承的。
    pass

'''关键是通过从Calculator那里继承calculate，并从Talker那里继承talk，它成了会说话的计算器。'''

#多重继承，是一个功能强大的工具。
tc = TalkingCalculator()   #覆盖Talker类的方法talk（导致它不可访问）
tc.calculate('1 + 2 * 3')
print(tc.talk())




'''
    复数形式的__bases__,你可使用它来获悉类的基类，而基类可能有多个。
    多重继承，应避免使用多重继承，因为在有些情况下，越使用越复杂。


    使用多重继承时，注意：如果多个超类以不同的方式实现了同一个方法
（即有多个同名方法），必须在class语句中小心排列这些超类，
因为位于前面的类的方法将覆盖位于后面的类的方法。




    如果Calculator类包含方法talk，那么这个方法将覆盖Talker类的方法talk（导致它不可访问）。

    class TalkingCalculator(Talker, Calculator):
        pass      #将导致Talker的方法talk是可以访问的。


    多个超类的超类相同时，查找特定方法或属性时访问超类的顺序称为方法解析顺序（ MRO），
它使用的算法非常复杂，但效果很好.

'''
