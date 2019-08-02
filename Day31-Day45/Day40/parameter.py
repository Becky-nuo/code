#不用提供参数


class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


#启用和关闭抑制功能
calculator = MuffledCalculator()
print(calculator.calc('10 / 2'))
print(calculator.calc('10 / 0'))   # 关闭了抑制功能

calculator.muffled = True
print(calculator.calc('10 / 0'))


try:
    1/0
except ZeroDivisionError:
    raise ValueError



#使用raise ... from ...语句(提供自己的异常上下文，也可使用None来禁用上下文)

try:
    1/0
    except ZeroDivisionError:
        raise ValueError from None



'''
    不用提供参数捕获异常后，如果要重新引发它（即继续向上传播）,
可调用raise且不提供任何参数。

    计算器类在与用户交互的会话中使用这个计算器时，抑制异常很有用；
但在程序内部使用时，引发异常是更佳的选择（此时应关闭“抑制”功能）。

    发生除零行为时，如果启用了“抑制”功能，方法calc将（隐式地）返回None。
换而言之，如果启用了“抑制”功能，就不应依赖返回值。

    关闭抑制功能时，捕获了异常ZeroDivisionError，但继续向上传播它。

'''
