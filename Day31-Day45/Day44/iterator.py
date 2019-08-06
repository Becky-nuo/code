#从迭代器创建序列


'''
    除了对迭代器和可迭代对象进行迭代（通常这样做）之外，还可将它们转换为序列。
    在可以使用序列的情况下，大多也可使用迭代器或可迭代对象（诸如索引和切片等操作除外）。
    
'''

#使用构造函数list显式地将迭代器转换为列表
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    
    def __iter__(self):
        return self
    
ti = TestIterator()
print(list(ti))
