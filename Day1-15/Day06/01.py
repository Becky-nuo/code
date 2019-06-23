Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#集合（集合无序可变，元素不能重复。集合的所有元素都是字典中的“键对象”，所以不能重复且唯一的

#一、集合创建和删除

#1.{}创建集合对象
>>> a={2,3,5}
>>> a
{2, 3, 5}

#2.add()添加元素
>>> a.add(7)
>>> a
{2, 3, 5, 7}
>>> a.add("mn")
>>> a
{2, 'mn', 3, 5, 7}

#set() 将列表、元组、等可迭代对象转成集合，如数据重复，则只保留一个
>>> a=['a','b','c','d']
>>> b=set(a)  #也可用copy()
>>> b
{'c', 'b', 'd', 'a'}

#remove() 删除指定元素
>>> a={10,20,30,40,50}
>>> a.remove(40)
>>> a
{10, 50, 20, 30}

#clear()清空整个集合
>>> a.clear()
>>> a
set()


#二、集合相关操作（并集、交集、差集等）
>>> a={1,2,3,'abc'}
>>> b={'cvb','zxc','abc'}
>>> a|b   #并集
{1, 2, 3, 'abc', 'cvb', 'zxc'}
>>> a&b   #交集
{'abc'}
>>> a-b   #差集
{1, 2, 3}
>>> a.union(b)   #并集
{1, 2, 3, 'abc', 'cvb', 'zxc'}
>>> a.intersection(b)  #交集
{'abc'}
>>> a.difference(b)    #差集
{1, 2, 3} 
