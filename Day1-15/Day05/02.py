'''
    1.随机生成1000个整数
    2.范围[20,100]
    3.升序输出所有不同的数字及其每个数字重复的次数
'''




import random

num_dirc = {}

#统计数字及对应的次数
for i in range (1000):
    num_key = random.randint(20,100)
    if num_key in num_dirc:
        num_dirc[num_key] += 1
    else:
        num_dirc[num_key] = 1
##排序，便历输出
for i in sorted(num_dirc.keys()):
    print('%d,%d' %(i,num_dirc[i]))
