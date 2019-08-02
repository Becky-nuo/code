
#捕获对象(在except子句中访问异常对象本身，可使用两个而不是一个参数)
'''(即便是在你捕获多个异常时，也只向except提供了一个参数——一个元组)

'''

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
    except (ZeroDivisionError, TypeError) as e:
        print(e)



#处理异常
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
    except:
        print('Something wrong happened ...')


'''用户想怎么做都可以'''

Enter the first number: "This" is *completely* illegal 123
Something wrong happened 




'''
    except子句也捕获两种异常，但由于你同时显式地捕获了对象本身，
因此可将其打印出来，让用户知道发生了什么情况。

    即使程序处理了好几种异常，还是可能有一些漏网之鱼。
（对于前面执行除法运算的程序，如果用户在提示时不输入任何内容就按回车键，
将出现一条错误消息，还有一些相关问题出在什么地方的信息（ 栈跟踪））。



    异常未被try/except语句捕获，这理所当然，因为你没有预测到这种问题，也没有采取相应的措施,
可以让程序马上崩溃，因为这样你就知道什么地方出了问题。

    捕获所有的异常很危险，因为这不仅会隐藏你有心理准备的错误，还会隐藏你没有考虑过的错误。

    应该使用except Exception as e来对异常对象进行检查。

    SystemExit和KeyboardInterrupt，因为它们是从BaseException（ Exception的超类）派生而来的。
'''
