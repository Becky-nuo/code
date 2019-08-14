#shelve 和 json


import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')
print(s['x'])



temp = s['x']
temp.append('d')
s['x'] = temp
print(s['x'])



#简单数据库应用程序
import sys, shelve
def store_person(db):'''让用户输入数据并将其存储到shelf对象中'''
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):  """让用户输入ID和所需的字段，并从shelf对象中获取相应的数据"""
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()

    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')


def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('文件路径.dat') # 你可能想修改这个名称

    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if name == '__main__':
    main()





'''

    函数open,将一个文件名作为参数，并返回一个Shelf对象，供你用来存储数据。

     一个潜在的陷阱至关重要的一点是认识到shelve.open返回的对象并非普通映射。

     查看shelf对象中的元素时，将使用存储版重建该对象，而当你将一个元素赋给键时，该元素将被存储。

     要正确地修改使用模块shelve存储的对象，必须将获取的副本赋给一个临时变量，并在修改这个副本后再次存储

     函数open的参数writeback设置为True，从shelf对象读取或赋给它的所有数据结构都将保存到内存（缓存）中，
并等到你关闭shelf对象时才将它们写入磁盘中。


程序里有趣的特征：
    所有代码都放在函数中，这提高了程序的结构化程度（一个可能的改进是将这些函数作为一个类的方法）。

    主程序位于函数main中，这个函数仅在__name__== '__main__'时才会被调用，在另一个程序中将这个程序作为模块导入，
再调用函数main。

    在函数main中，我打开一个数据库（ shelf），再将其作为参数传递给其他需要它的函数。

    调用strip和lower来修改读入一些值，因为仅当提供的键与存储的键完全相同时，它们才匹配。

    使用try和finally，是为确保数据库得以妥善的关闭。

    使用try和finally，程序终止时未妥善地关闭数据库，数据库文件可能受损，变得毫无用处。



'''
