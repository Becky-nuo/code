#python 中__len__

class Student(object):
    def __init__(self,*args):
        self.names = args

    def __len__(self):
        return len(self.names)

ss = Student('Bob','Ailce','Tim')
print(len(ss))



class Fib(object):
    def __init_(self, num):
        self.num = num

    def __str__(self):
        L=[0,1]
        for x in range(0,self.num-2):
            L.append(L[-1]+[-2])
        return str(L)

    def len(self):
        return self.num


print(len(Fib(10)))

