#range()函数（生成数列）
for i in range(2):  #产生序列
    print(i)


for m in range(2,9):  #指定区间的值
    print(m)


for n in range(0,10,3):  #指定数字开始并指定不同的数量
    print(n)


for h in range(-10,-100,-20):  #负数
    print(h)



'''
    range 对象是一个迭代器对象，用来产生指定范围的数字序列
    
    格式：
        range(start,end,[step])

    生成的数值序列start开始到end结束（不包含end），若没有写start，/
则默认从0开始，step是可选的步长，默认为1

'''
