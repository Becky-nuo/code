#嵌套函数（内部函数）


def f1():
    print("f1 running")

    def f2():
        print("f2 running")

    f2()

f1()


def printName(isChinese,name,familyName):
    def f2_print(a,b):
        print("{0} {1}".format(a,b))


    if isChinese:
        f2_print(familyName,name)   #中文名
    else:
        f2_print(name,familyName)   #英文名


printName(True,"小明","张")
printName(False,"Becky","chen")


'''
    1、在函数内部定义的函数
    2、封装-数据隐藏
    3、嵌套函数，可以让我们在函数内部避免复杂重复代码
'''
