#测试LEGB规则


print(type(str ))
#str = "global str"  #Glocal
def f1():



    #str = "f1"   #Enclosed
    def f2():
        #str = "f2"  #Local
        print(str)



    f2()



f1()




'''
    查找顺序：Local-->Enclosed-->Global-->Built in
    Local:指的是函数或者类的方法内部
    Enclosed:指的是嵌套函数（一个函数包裹另一个函数，闭包）
    Global:指的是模块中的全局变量
    Built in:指的是python为自己保留的特殊名称（NameError）


    如果某个name映射在局部（Local）命名空间中没有找到，接下来就会在/
    闭包作用域（Enclosed）进行、搜索，如果闭包作用域也没有找到，/
    python就会到全局（Glocal）命名空间在进行查找，最后会在内建/
    （Built in）命名空间搜索（如果一个名称在所有命名空间都没有找到，/
    就会产生一个NameError）。
'''
