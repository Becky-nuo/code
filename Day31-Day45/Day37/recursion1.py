#递归（阶乘和幂）


#计算数字n的阶乘（n × (n- 1) × (n - 2) × … × 1，可使用循环）

def factorial(n):
    result = n  #先将result设置为n
    for i in range(1, n):
        result *= i   #再将其依次乘以1到n- 1的每个数字，最后返回result
        return result


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):     #power(x, n),'x的n次幂'是将数字x自乘n - 1次的结果,即将n个x相乘的结果。
    result = 1
    for i in range(n):
        result *= x
        return result


'''
这是一个非常简单的小型函数，但也可将定义修改成递归式的。
对于任何数字x， power(x, 0)都为1。
n>0时， power(x, n)为power(x, n-1)与x的乘积。
如你所见，这种定义提供的结果与更简单的迭代定义完全相同。理解定义是最难的，而实现起来很容易。

'''
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)



'''
    1的阶乘为1,对于大于1的数字n，其阶乘为n - 1的阶乘再乘以n。

    函数调用factorial(n)和factorial(n – 1)是不同的实体。


    如果函数或算法复杂难懂，在实现前用自己的话进行明确的定义将大有裨益。
以这种“准编程语言”编写的程序通常称为伪代码。

    递归可以使用循环，很多情况下，使用循环的效率可能更高。
    使用递归的可读性更高，且有时要高得多，在你理解了函数的递归式定义时尤其如此。
'''
