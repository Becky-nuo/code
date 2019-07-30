#递归（二分查法,这种算法自然而然地引出了递归式定义和实现）



def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upperelse
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)




#在函数开头添加如下条件语句：
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1




        
'''现在，如果你没有提供上限和下限，它们将分别设置为序列的第一个位置和最后一个位置。'''

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
print(search(seq, 34))
print(search(seq, 100))





'''
    如果上限和下限相同，就说明它们都指向数字所在的位置，因此将这个数字返回;
否则，找出区间的中间位置（上限和下限的平均值），再确定数字在左半部分还是右半部分;
然后在继续在数字所在的那部分中查找。
    如果要查找的数字更大，肯定在右边；如果更小，它必然在左边。
    这种查找算法返回数字应该在的位置,如果这个数字不在序列中，那么这个位置上的自然是另一个数字。

    这些代码所做的与定义完全一致：如果lower == upper，就返回upper，即上限。
    如果还未达到基线条件，就找出中间位置，确定数字在它左边还是右边，再使用新的上限和下限递归地调用search。
    
    首先，你可使用列表方法index来查找。其次，即便你要自己实现这种功能，也可创建一个循环，
让它从序列开头开始迭代，直至找到指定的数字。使用index挺好，但使用简单循环可能效率低下。
    
'''
