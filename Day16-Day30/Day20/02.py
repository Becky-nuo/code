#python 中自定义排序函数

def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print(list(sorted([23,45,67,89,65],key=lambda x:x.upper())))



'''使用sorted()高阶函数给字符串排序'''
def cmp_ignore_case(s1,s2):
    a=s1.lower()
    b=s2.lower()

    if a<b:
        return -1
    if a>b:
        return 1
    return 0


print(list(sorted(['bob','abouut','Zoo','Credit'],key=lambda x:x[0].upper())))



'''
    python内置的sorted()函数可对list进行排序，但sorted()也是一个高阶函数，可以接收/
一个函数来实现自定义排序。比较函数的定义是：传入两个待比较的元素x,y如果x应该排在y/
的前面，返回-1,如果x应该排在y的后面，返回1。如果x和y相等，返回0。
