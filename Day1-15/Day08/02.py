#嵌套循环（一个循环体内可以嵌入另一个循环）

for b in range(10):  #生成序列0-9
    for c in range(5):  #循环5次
        print(b,end="\t")
    print()  #起换行的作用
