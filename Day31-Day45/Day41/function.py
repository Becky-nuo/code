
#异常和函数


def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    print(faulty())

def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')
print(ignore_exception())
print(handle_exception())



#使用模块中的函数warn(想发出警告，指出情况偏离了正轨)

from warnings import warn
warn("I've got a bad feeling about this.")
__main__:1: UserWarning: I've got a bad feeling about this.



from warnings import filterwarnings
filterwarnings("ignore")
warn("Anyone out there?")
filterwarnings("error")
print(warn("Something is very wrong!"))


filterwarnings("error")
print(warn("This function is really old...", DeprecationWarning))
filterwarnings("ignore", category=DeprecationWarning)
warn("Another deprecation warning.", DeprecationWarning)
print(warn("Something else."))



'''
    如果不处理函数中引发的异常，它将向上传播到调用函数的地方。
    如果在那里也未得到处理，异常将继续传播，直至到达主程序（全局作用域）。
    如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息。

    faulty中引发的异常依次从faulty和ignore_exception向外传播，最终导致显示一条栈跟踪消息。
    调用handle_exception时，异常最终传播到handle_exception，并被这里的try/except语句处理。


    警告只显示一次。如果再次运行最后一行代码，什么事情都不会发生。
    如果其他代码在使用你的模块，可使用模块warnings中的函数filterwarnings来抑制你发出的警告
（或特定类型的警告），并指定要采取的措施，如"error"或"ignore"。

    发出警告时，可指定将引发的异常（即警告类别），但必须是Warning的子类。
如果将警告转换为错误，将使用你指定的异常。另外，还可根据异常来过滤掉特定类型的警告。

'''
