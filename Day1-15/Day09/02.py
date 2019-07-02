#列表推导式(生成列表对象)


y=[x for x in range(1,5)] #循环遍历1,2,3,4
print(y)

q=[x*2 for x in range(1,60)if x&5==0]  #乘以2,添加条件过滤（if（被五整除））
print(q)

z = []
for x in range(1,60):
        if x%5==0:z.append(x*2)
print(z)

c=[a for a in "abcdefg"] #字符串
print(c)


cells=[(row,col)for row in range(1,10)for col in range(1,10)] #两嵌套循环
print(cells)

'''
    语法（中括号）：
    [表达式 for item in 可迭代对象]
或者：[表达式 foe item in 可迭代对象 if 条件判断
    
'''





#字典推导式

'''
    格式（大括号）：
    {key_expression :value_expression for 表达式 in 可迭代对象}

    字典推导式也可以增加if条件判断，多个for循环
'''

#统计文本中字符串出现的次数；
text='to be or not to be'
char_count={c:text.count(c) for c in text}
print(char_count)
