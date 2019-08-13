#创建生成器


#创建一个将嵌套列表展开的函数
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element



nested = [[1, 2], [3, 4], [5]]   #列表的列表,按顺序提供这些数字
for num in flatten(nested):
    print(num)

#list(flatten(nested))
     
     





'''

    迭代所提供嵌套列表中的所有子列表，然后按顺序迭代每个子列表的元素。

    包含yield语句的函数都被称为生成器。这可不仅仅是名称上的差别，生成器的行为与普通函数截然不同。


工作原理：
    生成器不是使用return返回一个值，而是可以生成多个值，每次一个。
每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。
被重新唤醒后，函数将从停止的地方开始继续执行。


    包装可迭代对象（可能生成大量的值），使用列表推导将立即实例化一个列表，从而丧失迭代的优势。

    直接在一对既有的圆括号内（如在函数调用中）使用生成器推导时，无需再添加一对圆括号。

    

'''