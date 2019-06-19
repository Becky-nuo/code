#统计字符串a中1的个数


#第一种
a='20190116'
b=a.count('1')
print(b)

#第二种
count=0
for i in a:
    if i=='1':
        count+=1
print(count)
    
