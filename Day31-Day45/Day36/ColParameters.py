
#收集参数


'''允许用户提供任意数量的参数很有用,每次只能存储一个姓名。'''

store(data, name1, name2, name3)  #允许用户提供任意数量的姓名。

def print_params(*params):
    print(params)  #这里好像只指定了一个参数，但它前面有一个星号。
    print_params('Testing')

print_params(1, 2, 3)(1, 2, 3) #注意到打印的是一个元组，因为里面有一个逗号。


参数前面的星号将提供的所有值都放在一个元组中，也就是将这些值收集起来。赋值时带星号的变量收集多余的值。它收集的是列表而不是元组中多余的值，但除此之外，这两种用法很像。下面再来编写一个函数

def print_params_2(title, *params):
    print(title)print(params)并尝试调用它:
        print_params_2('Params:', 1, 2, 3)
        Params:
            (1, 2, 3)         #星号意味着收集余下的位置参数。如果没有可供收集的参数， params将是一个空元组。
            print_params_2('Nothing:')  #与赋值时一样，带星号的参数也可放在其他位置（而不是最后），但不同的是，在这种情况下你需要做些额外的工作：使用名称来指定后续参数。

def in_the_middle(x, *y, z):
    print(x, y, z)
    in_the_middle(1, 2, 3, 4, 5, z=7)
    in_the_middle(1, 2, 3, 4, 5, 7)Traceback (most recent call last):   #星号不会收集关键字参数
print_params_2('Hmm...', something=42  #要收集关键字参数，可使用两个星号。


def print_params_3(**params):
               print(params)
               print_params_3(x=1, y=2, z=3)  #得到的是一个字典而不是元组。
def print_params_4(x, y, z=3, *pospar, **keypar):print(x, y, z)print(pospar)print(keypar)其效果与预期的相同。
               print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
               print_params_4(1, 2)1 2 3(){}  #不管在函数定义中的工作原理是否使用*和**，都可以函数调用中使用它们


def store(data, *full_names):
               for full_name in full_names:
               names = full_name.split()
               if len(names) == 2: names.insert(1, '')labels = 'first', 'middle', 'last'
               for label, name in zip(labels, names):
                   people = lookup(data, label, name)
                   if people:
                       people.append(full_name)
                   else:
                       data[label][name] = [full_name]  #这个函数调用起来与只接受一个姓名的前一版一样容易。



d = {}
init(d)
store(d, 'Han Solo')
store(d, 'Luke Skywalker', 'Anakin Skywalker')
lookup(d, 'last', 'Skywalker')['Luke Skywalker', 'Anakin Skywalker']
