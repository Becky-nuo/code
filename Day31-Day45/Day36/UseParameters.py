#练习使用参数


def story(**kwds):
    return 'Once upon a time,there was a ' \'{job} called {name}.'.format_map(*kwds)

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:          # 如果没有给参数stop指定值。
        start, stop = 0, start  # 就调整参数start和stop的值
        result = []



        i = start      # 从start开始往上数
        while i < stop:     # 数到stop位置
            result.append(i)    # 将当前数的数附加到result末尾
            i += step      # 增加到当前数和step（ > 0）之和
            return result


#尝试调用函数。

print(story(job='king', name='Li'))
print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']>
print(story(job='stroke of genius', **params))

print(power(2, 3))
print(power(3, 2))
print(power(y=3, x=2))

params = (5,) * 2
print(power(*params))

print(power(3, 3, 'Hello, world'))
print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
print(power(*interval(3, 7)))
