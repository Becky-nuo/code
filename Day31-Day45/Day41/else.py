#给try/except语句添加一个else子句



try:
    print('A simple task')
except:
    print('What? Something went wrong?')
else:
    print('Ah ... It went as planned.')



#使用else子句
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
    except:
        print('Invalid input. Please try again.')
    else:
        break



while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / yprint('x / y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break




'''
    没有引发异常时，才会跳出循环（这是由else子句中的break语句实现的）,
换句话说,只要出现错误，程序就会要求用户提供新的输入。

    使用空的except子句来捕获所有属于类Exception（或其子类）的异常。

    try/except语句中的代码可能使用旧式的字符串异常或引发并非从Exception派生而来的异常。


'''
