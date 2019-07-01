
#continue语句（结束本次循环）


#录入员工的薪资，打印输出录入的薪资和平均薪资
empNum=0
salarySum=0
salarys=[]
while True:
    s=input("请输入员工的薪资（按Q或q结束）")  #输入



    if s.upper()=='Q':
        print("录入完成，退出")
        break
    
    if float(s)<0:  #数据不正常就结束（无效），重新循环
        countinue
    empNum +=1   #员工数
    salarys.append(float(s))
    salarySum +=float(s)


print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))


'''
    continue语句用于结束本次循环，多个循环嵌套时，/
    continue也是应用于最近的一层循环。
    
'''
