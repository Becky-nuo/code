#规则(处理程序的可扩展性和灵活性都非常高,将注意力转向解析（对文本进行解读）了)



#标题规则：

class HeadlineRule:
    def condition(self, block): #如果文本块符合标题的定义，就返回True；否则返回False。
    def action(self, block, handler):

'''调用如handler.start('headline')、 handler.feed(block）和handler.end('headline')等方法。'''



                                            
#规则的超类

class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True






'''

    将规则定义为独立的对象，而不像初次实现中那样使用一条包含各种条件和操作的大型if语句。

    规则是供主程序（解析器）使用的。主程序必须根据给定的文本块选择合适的规则来对其进行必要的转换。

    方法condition返回一个布尔值，指出当前规则是否适用于处理指定的文本块。

    要实现复杂的解析规则，可能需要让规则对象能够访问一些状态变量，从而让它知道之前发生的情况或已应用了哪些规则。

    方法action将当前文本块作为参数，为了影响输出，必须能够访问处理器对象。适用的规则可能只有一个。

    使用了标题规则（这表明当前文本块为标题）后，就不能再试图使用段落规则。

    方法action，返回一个布尔值，指出是否就此结束对当前文本块的处理。

    调用处理程序的方法start、 feed和end，并将相应的类型字符串作为参数，再返回True（以结束对当前文本块的处理）。

    Rule类包含在模块rules中，这个模块的完整代码。

    方法condition由各个子类负责实现。 Rule类及其子类都放在模块rules中。



规则的功能:

    知道自己适用于那种文本块（ 条件）。
    对文本块进行转换（ 操作）。


每个规则对象都必须包含两个方法：

    condition和action。
    
    方法condition只需要一个参数：待处理的文本块。



'''





    

    









'''
