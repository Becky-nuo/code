#python 中类型转换

class Rational(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __init__(self):
        return self.a // self.b  #int

    def __float__(self):
        return float(self.a) / (self.b)  #float

print(float(Rational(7,2)))
print(float(Rational(1,3)))
