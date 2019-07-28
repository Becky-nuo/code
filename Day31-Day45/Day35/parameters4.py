
#关键字参数和默认值
'''前面使用的参数都是位置参数，因为它们的位置至关重要——事实上比名称还重要。'''


def hello_1(greeting, name):
    print('{}, {}!'.format(greeting, name))

def hello_2(name, greeting):
    print('{}, {}!'.format(name, greeting))

'''这两个函数的功能完全相同，只是参数的排列顺序相反。'''

print(hello_1('Hello', 'world'))
print(hello_2('Hello', 'world'))

print(hello_1(greeting='Hello', name='world')) #为了简化调用工作，可指定参数的名称。
print(hello_1(name='world', greeting='Hello')) #参数的顺序无关紧要,不过名称很重要。
print(hello_2(greeting='Hello', name='world'))


'''使用名称指定的参数称为关键字参数，主要优点是有助于澄清各个参数的作用。'''

store('Mr. Brainsample', 10, 20, 13, 5)
store(patient='Mr. Brainsample', hour=10, minute=20, day=13, month=5)

''' 虽然输入量多了，但每个参数的作用清晰明了。
    参数的顺序错了也没关系，因为关键字参数最大的优点在于，可以指定默认值。'''

def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))
print(hello_3())
print(hello_3('Greetings'))
print(hello_3('Greetings', 'universe'))
print(hello_3(name='Gumby'))


def hello_4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))

print(hello_4('Mars'))
print(hello_4('Mars', 'Howdy'))
print(hello_4('Mars', 'Howdy', '...'))
print(hello_4('Mars', punctuation='.'))
print(hello_4('Mars', greeting='Top of the morning to ya'))
print(hello_4())  #注意 如果给参数name也指定了默认值，最后一个调用就不会引发异常



''' 参数指定默认值后，调用函数时可不提供它！可以根据需要，一个参数值也不提供、提供部分参数值或提供全部参数值。
    使用位置参数就很好，只不过如果要提供参数name，必须同时提供参数greeting。
    如果只想提供参数name，并让参数greeting使用默认值呢？相信你已猜到该怎么做了。
    可以结合使用位置参数和关键字参数，但必须先指定所有的位置参数，否则解释器将不知道它们是哪个参数（即不知道参数对应的位置）。

'''
