
#函数的定义与调用

def test01():    #定义函数名
    print("*"*10)  #语句块
    print("@"*10)



print(id(test01))  #地址(给test01)
print(type(test01))  #类型
print(test01)  #  value值


test01()  #调用，可调用无数次
test01()
test01()

for i in range(10): #调用（循环调用10次）
    test01()

'''
    1、使用def定义函数，就是一个空格和函数名称
    2、python执行def时，会创建一个函数对象（python中一切都是对象），并绑定到函数名变量上

    格式：
    def 函数名 ([参数列表]):
        文档字符串
        函数体/若干语句
'''
