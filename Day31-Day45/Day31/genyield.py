#yield生成器实现斐波那契列数（congin:utf-8）

import time


'''普通的斐波那契数列实现'''
def fab1(max):
    n,a,b = 0,0,1
    while n<max:
        if n<20:
            print('->',b)
        a,b=b,a+b
        n=n+1


'''生成器算法实现斐波那契数列'''
def fab2(max):
    n,a,b = 0,0,1
    while n<max:
        yield b  #使用yield
        a,b = b,a+b
        n = n+1


def GeneratorDome():
    maxnum = 10000  #最大迭代数
    t1 = time.time()
    fab1(maxnum)
    t2 = time.time()
    print('Fab1 Total Time %.2f' % (10000*(t2-t1))+'ms')


    t3 = time.time()
    b = fab2(maxnum)
    t4 = time.time()
    print('Fab2 Total Time %.2f' % (10000*(t4-t3))+'ms')


if __name__=='__main__':
    GeneratorDome()



'''
    DESC:yield生成器你案例
    Author:伏草惟存
    Prompt:Code in python3 env


    斐波那契数列：1,1,2,3,5,8,13,21,34,55,89,144....
            从数列的第三项开始，后面每一项是前面两项之和。

    数学上的定义：F(0)=1,F(1)=1,...,f(n)=F(n-1)+F(n-2) (n>=2,n包含N*)

'''
