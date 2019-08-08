#双端队列（及其他集合）


from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)

deque([6, 0, 1, 2, 3, 4, 5])
print(q.pop())

print(q.popleft())
q.rotate(3)
print(q)

deque([2, 3, 4, 0, 1])
q.rotate(-1)
print(q)





'''
    按添加元素的顺序进行删除时，双端队列很有用。
    
    在模块collections中，包含类型deque以及其他几个集合（ collection）类型。

    与集合（ set）一样，双端队列也是从可迭代对象创建的，它包含多个很有用的方法。

    双端队列,它支持在队首（左端）高效地附加和弹出元素，而使用列表无法这样做。
还可高效地旋转元素（将元素向右或向左移，并在到达一端时环绕到另一端）。

    双端队列对象还包含方法extend和extendleft，其中extend类似于相应的列表方法。

    extendleft的可迭代对象中的元素将按相反的顺序出现在双端队列中。



'''
