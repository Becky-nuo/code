Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#编码(字符和数字对应)
>>> ord("A") # ord("") 字符转换成对应的Unicode码
65
>>> ord("陈")
38472
>>> chr(55) # chr() 十进制数字转换成对应的字符
'7'
>>> ord("诺")
35834



>>> #引号创建字符串(单引号或双引号)
>>> a="a'bcdef"  #头与尾的引号须一致，中间有引号无影响
>>> print(a)
a'bcdef
>>> b='yuiop"mn"'
>>> print(b)
yuiop"mn"
#多行（三个单引号或三个双引号）
>>> d='''a="qwe"
b="asd"
c="jkl"
d="34"'''
>>> print(d)
a="qwe"
b="asd"
c="jkl"
d="34"


 
#空字符串和len()函数
>>> c=''
>>> len(c)  #len() 表示查字符串的长度
0
>>> len(a)
7
>>> len("Becky")
5
>>> len("cvb晴天")  #汉字与英文字母的字符地位一致
5

#转义字符
>>> a="a\nb\nc"   #换行（\n）
>>> a
'a\nb\nc'
>>> print(a)
a
b
c
>>> b="a\' s d"   #单引号（\'）
>>> b
"a' s d"
>>> print(b)
a' s d
>>> print("aaaaaa\
bbbbb\
ddddd")          #续行（\）
aaaaaabbbbbddddd
'''
    \(在行尾)， 续行符
    \\    , 反斜杆符号
    \'    , 单引号
    \"    , 双引号
    \b    , 退格
    \n    , 换行
    \t    , 横向制表符
    \r    , 回车
'''


#字符串拼接
>>> "aa"+"bb"
'aabb'
>>> 3+5
8
>>> 3+"5"  #两边类型不同
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    3+"5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "aa""bb"   #加号可有可无，不影响
'aabb'

#字符串复制
>>> b='mon'*3  #3倍
>>> print(b)
monmonmon

