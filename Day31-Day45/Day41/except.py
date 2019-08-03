#异常处理


#假设有一个字典，你要在指定的键存在时打印与之相关联的值，否则什么都不做
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    if 'occupation' in person:
        print('Occupation:', person['occupation'])  #代码直观，但效率不高


def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError:
         pass

'''函数直接假设存在'occupation'键。如果这种假设正确，就能省点事：直接获取并打印值，
而无需检查这个键是否存在。如果这个键不存在，将引发KeyError异常，而except子句将捕获这个异常  '''



#检查一个对象是否包含属性write
try:   #访问属性write， 而没有使用它来做任何事情
    obj.write
except AttributeError:  #AttributeError异常，说明对象没有属性write，否则就说明有这个属性
    print('The object is not writeable')
else:
    print('The object is writeable')



'''
    出现异常时程序终止并显示栈跟踪消息，可添加必要的try/except或try/finally语句（或结合使用）来处理它。

异常处理：
    使用条件语句来达成异常处理实现的目标，但不自然，可读性也不高。
    使用if/else完成时看似很自然，但实际上使用try/except来完成要好得多。


    检查对象是否包含特定的属性时， try/except也很有用。

    使用if/else，使用try/except语句更自然，也更符合Python的风格。

'''
