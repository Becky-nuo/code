#参数工作原理


#函数内部给参数赋值
def try_to_change(n):
    n = 'Mr.Li'

name = 'Mrs.Chen'
try_to_change(name)  # try_to_change把新值赋给了参数n
print(name)   



name ='Mrs.chen'
n = name   #与传递参数的效果几乎一样
n = 'Mr.Li'  #在函数内进行
print(name)



#字符串（数和元组）
def change(n):
    n[0]= 'Mr.Li'
    names = ['Mrs.chen','Mrs.Zhang']
    change(names)
#print(names)
    
names = ['Mrs.chen','Mrs.Zhang']
n = names     #再次假装传递名字作为参数
n[0] = 'Mr.Li'  #修改列表
print(names)

names = ['Mrs.chen','Mrs.Zhang']
n = names[:]
print(n is names)
print(n == names)  #现在n 和 names包含两个相等但不同的列表

'''如果想修改n，也不会影响names'''
n[0] = 'Mr.Li'
print(n)
print(names)


'''
    变量n变了，但变量name没变（是一个完全不同的变量）
    函数内部重新关联参数（替换为新值）时，函数外部的变量不受影响


    字符串（以及数和元组）是不可变的，不能修改参数，只能替换为新值
    函数内修改了参数，但这个示列与前一个示列之间存在一个重要的不同

    列表赋给两个变量时，这两个变量将同时指向列表
    序列执行切片操作时，返回的切片都是副本

参数n包含的是副本，因此原始列表是安全的
'''
