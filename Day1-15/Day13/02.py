#nonlocal的用法


a=100

def f1():
    b = 10

    def f2():
        nonlocal b    #声明外部函数的局部变量
        print("f2 b:",b)
        b = 20

        global a  #声明全局变量
        a = 1000


    f2()
    print("f1 b:",b)


f1()
print("a:",a)
    
