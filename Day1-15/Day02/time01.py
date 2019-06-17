
import time
time01 = time.time()    #起始时刻


a=""
for i in range(10000000):
    a += "abc"


time02 = time.time()   #终止时刻

print("运算时刻： "+str(time02-time01))



time03 = time.time()   #起始时刻
li = []
for i in range(10000000):
    li.append("abc")

a="".join(li)
time04=time,time()  #终止时刻
print("运算时间："+str(time04-time03))
      
