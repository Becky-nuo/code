#修改参数

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Maguns Lie Hetland'
storage['first'] ['Maguns'] = {me}
storage['middle']['Lie'] = {me}
storage['last']['Hetland'] = {me}

print(storage['Middle']['Lie'])



my_sister = 'Anne Lie Hetland'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)
print(storage['first']['Anne'])
print(storage['middle']['Lie'])

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}  #这里只是将初始化语句移到了一个函数中

storage = {}
init(storage)
print(storage)  #函数承担了初始化职责，让代码的可读性高了很多。
