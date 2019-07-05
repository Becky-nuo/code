#eval()函数

s="print('abcbdefg')"
eval(s)



a = 10
b = 20
c=eval("a+b")  #a+b可以从外面传进来
print(c)

dict1 = dict(a=100,b=200)

d = eval("a+b",dict1) #取dict1里面的a，b值
print(d)


'''
    功能：将字符串str当成有效的表达式来求值并返回计算结果
    语法：eval(source,[global],[locals]) -> value
    参数：
        source:一个python表达式或函数compile()返回的代码对象
        global:可选，必须是dictionary
        locals:可选，任意映射对象
    
'''
