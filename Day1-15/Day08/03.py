
#break（结束整个循环）

while True:
    a=input("输入一个字符（输入Q或q时退出）")
    if a=='q' or a=='Q':
        print("循环结束，退出")
        break
    else:
        print(a)


'''
    break语句可用来while和for循环，用来结束整个循环，/
    当有嵌套循环时，break语句只能跳出最近一层的循环。
    
'''
