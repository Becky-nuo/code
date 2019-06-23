

#求平均值与和
a =[1,2,3,4,5,6,7,8,9,10]
sum=0
b = len(a)
print("这个数组的长度为：",b)
for i  in a:
 sum =sum +i
print("这个数组之和为：",sum)
print("这个数组平均数为",sum/b)


#最大值、最小值
b=[12,23,434,56]

print("最大值",max(b))

print("最小值",min(b))


#set() 去除列表里重复的元素
c=[11,22,33,44,55,22]
d=set(c)
print(d)


#集合
e=[1,2,3,4,5,6,7,8]
f=[10,20,30,40,50]
i=set(e)
j=set(f)
print(i,j)
