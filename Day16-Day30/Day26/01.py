#python 中的数学运算

class Rational(object):
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def __add__(self,r):
        return Rational(self.p * r.q + self.q * r.p,self.q * r.q)

    def __str__(self):
        return '%s/%s' % (self.p,self.q)
    repr__ = __str__


r1 = Rational(1,3)
r2 = Rational(1,2)
print(r1 + r2)


 

    

'''
    1、python提供的基本数据类型int,float可以做整数和浮点数的四则运算以及乘方等运算。
    2、四则运算不局限于int和folat还可以是有理数，矩阵等

'''
    
