#接口和内省(概念与多态相关)




print(hasattr(tc, 'talk'))  #检查属性talk是否是可调用的。
hasattr(tc, 'fnord')   #tc包含属性talk,但没有属性fnord



print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))

'''这里没有在if语句中使用hasattr并直接访问属性，
而是使用了getattr（它让我能够指定属性不存在时使用的默认值，这里为None），
然后对返回的对象调用callable。'''




'''setattr与getattr功能相反，可用于设置对象的属性：'''

setattr(tc, 'name', 'Mr. Gumby')
print(tc.name'Mr. Gumby)'




'''

    假定对象能够完成你要求它完成的任务,如果不能完成，程序将失败。
通常，你要求对象遵循特定的接口（即实现特定的方法），但如果需要，
也可非常灵活地提出要求：不是直接调用方法并期待一切顺利，
而是检查所需的方法是否存在；如果不存在，就改。


    处理多态对象时，你只关心其接口（协议）——对外暴露的方法和属性。
    在Python中，不显式地指定对象必须包含哪些方法才能用作参数。



    要查看对象中存储的所有值，可检查其__dict__属性,
如果要确定对象是由什么组成的，应研究模块inspect。


    这个模块主要供高级用户创建对象浏览器（让用户能够以图形方式浏览Python对象的程序）
以及其他需要这种功能的类似程序



'''
