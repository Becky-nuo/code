#使用递归函数，计算阶乘


def factorial(n):

    if n==1:       #停止条件
        return 1  #返回
    else:
        return n*factorial(n-1)


result = factorial(5)  #5!=5*4*3*2*1
print((result))
