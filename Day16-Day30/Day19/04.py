#filter()函数

'''filter的主要作用是通过function对iterable中元素进行过滤，/
并返回一个迭代器（iterator）,其中是function返回Ture的元素。'''



def is_even(x):
    return x%2==0

a=list(filter(is_even,range(10)))
print(a)




b=[x for x in range(10)]
print(list(filter(lambda x : x%2 ==0,b)))

'''因为filter返回的是一个iterator,所以输出的时候需要用list进行转换'''





c=[x for x in range(0,10)]
print(list(filter(None,c)))

'''filter的第一个参数传入了None，所以在迭代过程中，0被判断为False从而被过滤，/
1-9被保留下来，这个方法可以替代for循环的数据拾取。
