#解析器



class Parser:
'''读取文本文件、应用规则并控制处理程序的解析器'''
    def __init__ (self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)

        for rule in self.rules:
            if rule.condition(block):
                last = rule.action(block, self.handler)
                if last: break  #变量为True时退出for循环
    self.handler.end('document')
    block = filter(block, self.handler)





'''
    使用一个处理程序以及一系列规则和过滤器将纯文本文件转换为带标记的文件（这里是HTML文件）。

    构造函数、添加规则的方法、添加过滤器的方法以及对文件进行解析的方法。

    构造函数将提供的处理程序赋给一个实例变量（属性），再初始化两个列表：一个规则列表和一个过滤器列表。

    方法addRule在规则列表中添加一个规则。

    方法addFilter与方法addRule相似，在过滤器列表中添加一个过滤器，但之前要先创建过滤器。

    过滤器就是一个函数，调用re.sub将参数指定为合适的正则表达式（模式）和处理程序中的替换函数（ handler.sub(name)）。

    调用处理程序的方法 start('document')开头并 ,以调用处理程序的方法end('document')结束。

    迭代文本文件中的所有文本块。对于每个文本块，它都应用过滤器和规则。

    过滤器就是调用函数filter，并以文本块和处理程序作为参数，再将结果赋给变量block。

    规则适用，就调用rule.action，并将文本块和处理程序作为参数。

    方法action返回一个布尔值，指出是否就此结束对当前文本块的处理。

    将方法action的返回值赋给变量last，再在这个变量为True时退出for循环。




'''
