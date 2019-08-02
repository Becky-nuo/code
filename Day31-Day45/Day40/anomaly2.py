#异常类（）


#自定义异常类（内置异常涉及的范围很广）


class SomeCustomException(Exception):
    pass


#捕获异常


x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)



'''这个程序运行正常，直到用户输入的第二个数为零。'''

print(Enter the first number)
print(nter the second number)



try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!") #使用一条if语句来检查y的。


'''
    要使用特殊的错误处理代码对超光速推进装置错误进行处理，就必须有一个专门用于表示这些异常的类。
    创建异常类,要像创建其他类一样，但务必直接或间接地继承Exception（这意味着从任何内置异常类派生都可以）。
    
    异常比较有趣的地方是可对其进行处理，通常称之为捕获异常，可使用try/except语句。
假设你创建了一个程序，让用户输入两个数，再将它们相除。


    为捕获这种异常并对错误进行处理（这里只是打印一条对用户更友好的错误消息）。
    如果这个程序执行的除法运算更多，则每个除法运算都需要一条if语句，而使用try/except的话只需要一个错误处理程序。
    异常从函数向外传播到调用函数的地方。如果在这里也没有被捕获，异常将向程序的最顶层传播。
这意味着你可使用try/except来捕获他人所编写函数引发的异常。
    

'''
