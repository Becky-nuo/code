#多个except子句



Enter the first number:
    Enter the second number: "Hello, world!"



try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)

except ZeroDivisionError:
    print("The second number can't be zero!")

except TypeError:
    print("That wasn't a number, was it?")





#使用一个except子句捕获多种异常,在一个元组中指定这些异常

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
    except (ZeroDivisionError, TypeError, NameError):
        print('Your numbers were bogus ...')




'''
    多个 except 子句如果你运行前一节的程序，并在提示时输入一个非数字值，将引发另一种异常。

    由于该程序中的except子句只捕获ZeroDivisionError异常，这种异常将成为漏网之鱼，导致程序终止。
为同时捕获这种异常，可在try/except语句中再添加一个except子句。

    异常处理并不会导致代码混乱，而添加大量的if语句来检查各种可能的错误状态将导致代码的可读性极差。



    用户输入字符串、其他非数字值或输入的第二个数为零，都将打印同样的错误消息。
    不断地要求用户输入数字，到能够执行除法运算为止.

    在except子句中，异常两边的圆括号很重要,一种常见的错误是省略这些括号

'''
