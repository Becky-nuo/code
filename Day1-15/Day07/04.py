#for语句
d = ["abc","嗯嗯","def","mnl"]
for x in d:
    print(x)

for e in (10,20,30):  #元组
    print(e)

for j in "abcdefg":
    print(j)


'''
    格式：
    for  变量  in  可迭代对象:
        循环体语句


    可迭代对象：
    1、元组、列表、字符串
    2、字典
    3、迭代器对象（iterator）
    4、生成器函数（generator）
