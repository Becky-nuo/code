#生成器的使用


#通用生成器


def generator():
    yield 1

print(generator)
print(generator())




'''

    生成器每次请求值时，都将执行生成器的代码，直到遇到yield或return。yield意味着应生成一个值，
而return意味着生成器应停止执行（即不再生成值；仅当在生成器调用return时，才能不提供任何参数）。
    

    生成器是包含关键字yield的函数，但被调用时不会执行函数体内的代码，而是返回一个迭代器。

    生成器由两个单独的部分组成： 生成器的函数和生成器的迭代器。生成器的函数是由def语句定义的，
其中包含yield。生成器的迭代器是这个函数返回的结果。

    对于生成器的函数返回的迭代器，可以像使用其他迭代器一样使用它。

'''






#生成器的方法

def repeater(value):
    while True:
        new = (yield value)  #使用圆括号将yield表达式括起来(返回值)
        if new is not None: value = new

#使用生成器：
r = repeater(42)
print(next(r))

print(r.send("Hello, world!"))



'''
    生成器的方法在生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。
    
通信渠道包含两个端点:
    外部世界：外部世界可访问生成器的方法send，这个方法类似于next， 但接受一个参数
            （要发送的“消息”，可以是任何对象）。
            
    生成器：在挂起的生成器内部， yield可能用作表达式而不是语句。换而言之，当生成器新运行时，
yield返回一个值——通过send从外部世界发送的值。如果使用的是next，yield将返回None。


    生成器被挂起（即遇到第一个yield）后，使用send（而不是next）才有意义。
要在此之前向生成器提供信息，可使用生成器的函数的参数。

    如果一定要在生成器刚启动时对其调用方法send，可向它传递参数None。



生成器另外两个方法：
    方法throw：用于在生成器中（ yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
    
    方法close：用于停止生成器，调用时无需提供任何参数。
(由 Python 垃圾收 集 器在 需要 时 调用)也是基于异常的 ：在 yield 处 引 发GeneratorExit异常。
因此如果要在生成器中提供一些清理代码，可将yield放在一条try/finally语句中。























