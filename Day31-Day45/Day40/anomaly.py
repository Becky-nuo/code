#异常（Python使用异常对象来表示异常状态，并在遇到错误时引发异常）


print(1 / 0)



#raise语句


print(raise Exception)  #内置异常类Exception,引发的是通用异常，没有指出出现了什么错误。
print(raise Exception('hyperdrive overload')) #添加了错误消息hyperdrive overload。



print(aise ArithmeticError)

'''


    异常对象未被处理（或捕获）时，程序将终止并显示一条错误消息（ traceback）。
    每个异常都是某个类（这里是ZeroDivisionError）的实例。
你能以各种方式引发和捕获这些实例，从而逮住错误并采取措施，而不是放任整个程序失败。
    出现问题时，将自动引发异常。

    raise 语句要引发异常，可使用raise语句，并将一个类（必须是Exception的子类）或实例作为参数。
将类作为参数时，将自动创建一个实例。



表8-1 一些内置的异常类

                 类 名                   描  述
                 
                Exception           几乎所有的异常类都是从它派生而来的
                AttributeError      引用属性或给它赋值失败时引发
                OSError             操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
                IndexError          使用序列中不存在的索引时引发，为LookupError的子类KeyError 使用映射中不存在的键时引发，为LookupError的子类
                NameError           找不到名称（变量）时引发
                SyntaxError         代码不正确时引发
                TypeError           将内置操作或函数用于类型不正确的对象时引发
                ValueError          将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
                ZeroDivisionError   在除法或求模运算的第二个参数为零时引发
