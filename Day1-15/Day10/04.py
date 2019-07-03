#测试函数也是对象

def test01():
    print("abcdef")


test01()  #调用

c = test01  #把test01的值拷贝给c
c()


print(id(test01))
print(id(c))
print(type(c))




'''
    内置函数对象会自动创建
    标准库的第三方库函数，通过import导入模块时，会执行模块的def语句
'''
