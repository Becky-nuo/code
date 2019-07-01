
#循环代码优化

'''
    1.尽量减少循环内部不必要的计算
    2.嵌套循环中，尽量减少内部循环的计算，尽量减少内层循环的计算，尽可能向外放
    3局部变量查询较快，尽量使用局部变量(性能要求高，循环次数高)

'''


import time

start=time.time()
for i in range(1000):
    result=[]
    for m in range(1000):
        result.append(i*1000+m*100)


end = time.time()
print("耗时：{0}".format((end-start)))


start2 = time.time()
for i in range(1000):
    result=[]
    c=i*1000
    result.append(c+m*100)  #把i*1000提到内循环的外面去了，用c表示，性能提高了
        
end2 = time.time()
print("耗时：{0}".format((end2-start2)))



'''
    1、连接多个字符串，使用join（）而不使用“+”（产生新的对象）
    2、列表进行元素插入和删除，尽量在列表尾部操作，不然后面的数据要重新拷贝，很浪费时间。

'''
