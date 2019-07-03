#函数返回值

def add(a,b):
    print("计算两个数的和，{0},{1},{2}".format(a,b,(a+b)))
    return a+b


def test01():
    print("abc")
    print("cvb")


    return  #作用：1、返回值  2、结束函数的执行

    print("hello")


def test02(x,y,z):
    return(x*10,y*10,z*10)


c = add(30,40)
print(add(30,40))
d = test01()
print(d)


print(test02(4,3,2))


'''
    1、如果函数体中包含return语句，则结果函数执行并返回值。
    2、如果函数体中不包含return语句，则返回None值。
    3、要返回多个值返回值，使用列表、元组、集合将多个值“存起来”。
'''
