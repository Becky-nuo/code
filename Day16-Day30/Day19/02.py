#reduce()函数

import reduce

a=list(reduce(lambda x,y:x//y,(16,4))) #16//4=4
print(a)

b=list(reduce(lambda x,y:x//y,(16,4,2)))#16//4//2=2
print(b)


'''
    1、reduce接受两个参数，一个是函数，函数必须接受两个参数，/
第二个是序列，reduce把结果继续和序列的下一个元素做累积计算。
    2、reduce函数，作用是返回第一个数除以第二个数，产生结果再去除第三个数，以此类推。

'''
