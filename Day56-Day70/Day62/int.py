
>>> 12
12
>>> 0b101   #二进制
5
>>> 0o9    #八进制（没有9）
SyntaxError: invalid token
>>> 0o10   #八进制
8
>>> 0xff   #十六进制
255
>>> 0xf
15
>>> 0x10
16

#int()类型转换
>>> int(3.2226)  #浮点数直接舍去小数部分，
3
>>> int(3.9999)
3
>>> int(True)  #布尔值
1
>>> int(False)
0
>>> int("23456") #字符串符合整数格式，直接转成对应整数
23456
>>> int("23456abcde")


#自动转型（整数和浮点数混合运算的时候，表达式 结果自动转型为浮点数）
>>> a=3+4.1
>>> a
7.1


'''
    0b或0B，二进制   0  1
    0o或0O，八进制   0  1  2  3  4  5  6  7
    0x或0X，十六进制 0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f

'''



>>> googol=10**100  #10的100次方
>>> googol
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>>



