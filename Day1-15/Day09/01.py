#使用zip()并行迭代

for i in {1,2,3}:
    print(i)

names=("小明","小天","小张","小丽")
ages=(15,18,23,25)
jobs=("学生","老师","程序员")

#zip()
for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

print()   


#range()
for i in range(3):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))
