#python中偏函数

import functools

def sort(data,lower):
    if lower==True:
        data=map(lambda x:x.lower(),data)
    return sorted(data)

sorted_ignore_case = functools.partial(sorted,lower=True)

print(sorted_ignore_case(['bob','about','zoo','Credit']))



#把functools.partial调用成一个简单的函数
import functools

sorted_ignore_case = functools.partial(sorted,key = lambda s:s[0].upper())

print(sorted_ignore_case(['bob','about','zoo','Credit']))


'''
    1、当一个函数有很多参数时，调用者需要提供多个参数，减少参数个数，可以简化调用者的负担。
    2、functools.partial就是帮助我们创建一个偏函数。
    3、functools.partial可以把一个参数多的函数变成一个参数少的函数，少的参数需要在创建时指定默认值。
'''    
    
