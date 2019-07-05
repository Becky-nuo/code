#可变参数
'''
    1、*param(一个星号)，将多个参数收集到一个“元组”对象中
    2、**param(两个星号)，将多个参数收集到一个“字典”对象中
'''

def test01(a,b,*c):  #元组
    print(a,b,c)
test01(2,3,5,6,7)



def test02(c,d,**f):   #字典
    print(c,d,f)
test02(4,5,neme='小明',age=18)




def test03(e,m,*n,**k):
    print(e,m,n,k)

test03(3,4,5,6,name='小明',age=18)


#强制命名参数

def test04(*t,f,h):
    print(t,f,h)
#test04(2,3,4,5)   会报错，由于a为可变参数，将2,3,4,5全部收集，造成f,n没有赋值

test04(2,3,f=4,h=5)   #命名参数


#在带星号的“可变参数”后面增加新的参数时，必须在调用的时候“强制命名参数”。
