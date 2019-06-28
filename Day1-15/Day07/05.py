
#遍历字符串中的字符
for a in list("abcdef"):
    print(a)




#遍历字典
a={"name":"小明","age":20,"job":"student"}
for x in  a:          #遍历字典所有的key
    print(x)
for x in a.keys():    #遍历字典所有的key
    print(x)
for x in a.values():  #遍历字典所有的value
    print(x)
for x in a.items():   #遍历字典所有的“键值对”
    print(x)
