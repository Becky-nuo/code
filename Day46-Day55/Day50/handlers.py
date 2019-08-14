#处理程序的超类(提高灵活性)




class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
                return result
        return substitution






#假设HTMLRenderer是Handler的子类

import re    
from handlers import HTMLRenderer
handler = HTMLRenderer()

handler.sub('emphasis') #将返回一个函数substitution

re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test')#在re.sub语句中使用这个函数




'''
    将是所有处理程序的超类，负责处理一些管理性细节。

    使用字符串表示文本块的类型,并将这样的字符串提供给处理程序将很有用。

    可添加一些通用方法，如start(type)、 end(type)和sub(type)。

    通用方法start、 end和sub检查是否实现了相应的方法（例如， start('paragraph')
检查是否实现了start_paragraph）。




    方法callback负责根据指定的前缀（如'start_'）和名称（如'paragraph'）查找相应的方法。

    使用getattr并将默认值设置为None实现的。如果getattr返回的对象是可调用的，就使用额外提供的参数调用它。
调用handler.callback('start_', 'paragraph')时，将调用方法handler.start_paragraph且不提供任何参数,如果start_paragraph存在的话。

    方法start和end都是辅助方法，它们分别使用前缀start_和end_调用callback。
    
    方法sub稍有不同。它不直接调用callback，而是返回一个函数，这个函数将作为替换函数传递给re.sub
（这就是它只接受一个匹配对象作为参数的原因所在）。
    





'''
