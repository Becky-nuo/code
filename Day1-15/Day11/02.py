#测试局部变量、全局变量的效率

import math
import time

def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}".format((end-start)))




def test02():
    b=math.sqrt
    start=time.time()
    for i in range(10000000):
        b(30)
    end=time.time()
    print("耗时{0}".format((end-start)))



test01()
test02()
    
