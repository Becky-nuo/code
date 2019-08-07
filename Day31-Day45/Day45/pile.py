#堆合、堆和双端队列


#集合,是由模块sets中的Set类实现的。


print(set(range(10)))  #在不提供任何参数的情况下调用set。

print(type({})) #花括号来创建空集合，因为这将创建一个空字典

print({0, 1, 2, 3, 0, 1, 2, 3, 4, 5})  #集合中元素的排列顺序是不确定的

print({'fee', 'fie', 'foe'})



a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))
print(a | b) 



c = a & b
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a))
print(c >= a)
print(a.intersection(b))

print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())
print(a.copy() is a)


my_sets = []
for i in range(10):
    my_sets.append(set(range(i, i+5)))

print(reduce(set.union,my_sets))



a = set()
b = set()
print(a.add(b))
print(a.add(frozenset(b)))  #frozenset类型，它表示不可变（可散列）的集合




'''

    Python支持一些较常用的，其中的字典（散列表）和列表（动态数组）是Python语言的有机组成部分。

    集合是可变的，因此不能用作字典中的键。

    集合只能包含不可变（可散列）的值，因此不能包含其他集合。
'''
    


