#random（编写模拟程序或生成随机输出的程序）



from random import *
from time import *
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

random_time = uniform(time1, time2)

print(asctime(localtime(random_time)))


from random import randrange  #掷骰子的机制,使用randrange和for循环实现的。
num = int(input('How many dice? '))
sides = int(input('How many sides per die? '))
sum = 0

for i in range(num):
    sum += randrange(sides) + 1
    print('The result is', sum)


# 文件名.py

import fileinput, random
fortunes = list(fileinput.input())
print(random.choice(fortunes))




'''
    函数生成的数字好像是完全随机的，但它们背后的系统是可预测的,如果你要求真正的随机（如用于加密或实现与安全相关的功能），
应考虑使用模块os中的函数urandom。

    random.random是最基本的随机函数之一，它返回一个0~1（含）的伪随机数。

    函数random.getrandbits以一个整数的方式返回指定数量的二进制位。向函数random.uniform提供了两个数字参数a和b时，
它返回一个a~b（含）的随机（均匀分布的）实数。

    函数random.randrange是生成随机整数的标准函数。

    randrange(1, 11)或randrange(10) + 1,生成一个1~10（含）的随机整数。

    uniform(0, 360)，随机角度，函数random.randrange是生成随机整数的标准函数。

    函数random.choice从给定序列中随机（均匀）地选择一个元素。
    函数random.shuffle随机地打乱一个可变序列中的元素，并确保每种可能的排列顺序出现的概率相同。
    函数random.sample从给定序列中随机（均匀）地选择指定数量的元素，并确保所选择元素的值各不相同。


    模块random中一些重要的函数:

    函 数                                       描 述
    random()                            返回一个0~1（含）的随机实数
    getrandbits(n)                      以长整数方式返回n个随机的二进制位
    uniform(a, b)                       返回一个a~b（含）的随机实数
    randrange([start], stop, [step])    从range(start, stop, step)中随机地选择一个数
    choice(seq)                         从序列seq中随机地选择一个元素
    shuffle(seq[, random])              就地打乱序列
    seqsample(seq, n)                   从序列seq中随机地选择n个值不同的元素函数

    




'''
