#模拟生成器(使用普通函数模拟生成器)



def flatten(nested):
    result = []
    try:                # 不迭代类似于字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
        return result


'''

    这种方法并不能模拟所有的生成器，但可模拟大部分生成器。
比如：无穷生成器，因为不能将生成器的值存储到一个列表里。

    较老的python版本，也无法使用生成器。
    

'''

