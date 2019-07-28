#编写获取人员姓名的函数和编写存储人员姓名的函数


def lookup(data, label, name):
    return data[label].get(name)  #函数lookup接受参数
label（如'middle'）和name（如'Lie'）#返回一个由全名组成的列表。


lookup(storage, 'middle', 'Lie')['Magnus Lie Hetland']

'''返回的是存储在数据结构中的列表。因此如果对返回的列表进行修改，将影响数据结构。/
（未找到任何人时除外，因为在这种情况下返回的是None。） '''


#人员存储到数据结构中的函数
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:people.append(full_name)
            else:data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
lookup(MyNames, 'middle', 'Lie')['Magnus Lie Hetland']


store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
lookup(MyNames, 'first', 'Robin')['Robin Hood', 'Robin Locksley']
store(MyNames, 'Mr. Gumby')
lookup(MyNames, 'middle', '')['Robin Hood', 'Robin Locksley', 'Mr. Gumby']  #如果有多个人的名字、中间可同时获取这些人员


'''
函数store执行如下步骤:
    (1) 将参数data和full_name提供给这个函数。这些参数被设置为从外部获得的值。
    (2) 通过拆分full_name创建一个名为names的列表。
    (3) 如果names的长度为2（只有名字和姓），就将中间名设置为空字符串。
    (4) 将'first'、 'middle'和'last'存储在元组labels中（也可使用列表，这里使用元组只是为了省略方括号）。
    (5) 使用函数zip将标签和对应的名字合并。


每个标签-名字对执行如下操作：
1、获取属于该标签和名字的列表.
q2、将full_name附加到该列表末尾或插入一个新列表。

'''


