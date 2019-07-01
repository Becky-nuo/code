
#else语句

#录入4位员工的薪资，打印输出录入的薪资的平均薪资并提示已经录入
salarySum=0
salarys=[]
for i in range(4):
    s=input("请输入4名员工的薪资（按Q或q结束）")  #输入



    if s.upper()=='Q':
        print("录入完成，退出")
        break
    
    if float(s)<0:  #数据不正常就结束（无效），重新循环
        countinue
        
    salarys.append(float(s))
    salarySum +=float(s)
else:
    print("你已经全部录入4名员工的薪资")


print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/4))


'''
    while、for循环可以带一个else语句（可选）。
    如果for、while语句没有被break语句结束，则会执行else子句，否则不执行。
    语法格式：
    while 条件表达式：
    else:
        语句块

    或者:
    for 变量 in 可迭代对象：
        循环体
    else：
        语句块


    while循环中断以后，被中断的情况下else是不执行的
    循环正常结束，else会执行。
'''
