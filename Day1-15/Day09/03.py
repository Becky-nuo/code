#集合推导式（生成集合） 不可重复


b = {x for x in range(1,100) if x%9==0}
print(b)

'''
    集合推导式与列表推导式的语法格式类似
    格式（大括号）：
    {表达式 for item in 可迭代对象}
或者：{表达式 for item in 可迭代对象 if 条件判断}
    
'''

#生成器推导式（生成元组） (小括号)  元组是没有推导式的

a=(x for x in range(10))
#print(a)  #生成生成器
#print(tuple(a))  #查看生成器里的内容


for x in a:  #a为生成器对象,生成器是可迭代对象,只能使用一次
    print(x,end=",")
print(tuple(a)) #空
