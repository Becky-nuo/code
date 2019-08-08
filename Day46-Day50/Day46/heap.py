#堆(是一种优先队列)

    
from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []

for n in data:
    heappush(heap, n) #函数heappush用于在堆中添加一个元素

print(heap)
heappush(heap, 0.5)
print(heap)



print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)



heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap) #函数heapify通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）。
print(heap)



print(heapreplace(heap, 0.5)) #函数heapreplace从堆中弹出最小的元素，再压入一个新元素
print(heap)
print(heapreplace(heap, 10))
print(heap)




'''

    优先队列让你能够以任意顺序添加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。
    Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。

    函数heappush不能将它用于普通列表，而只能用于使用各种堆函数创建的列表。（元素的顺序很重要）


    堆特征（ heap property）：位置i处的元素总是大于位置i // 2处的元素（反过来说就是小于位置2 * i和2 * i + 1处的元素）。

    函数heappop弹出最小的元素（总是位于索引0处），并确保剩余元素中最小的那个位于索引0处（保持堆特征）。

    nlargest(n, iter)和nsmallest(n, iter)， :分别用于找出可迭代对象iter中最大和最小的n个元素。



    模块heapq中一些重要的函数

        函 数                     描 述
    heappush(heap, x)       将x压入堆中
    heappop(heap)           从堆中弹出最小的元素
    heapify(heap)           让列表具备堆特征
    heapreplace(heap, x)    弹出最小的元素，并将x压入堆中
    nlargest(n, iter)       返回iter中n个最大的元素
    nsmallest(n, iter)      返回iter中n个最小的元素

'''




