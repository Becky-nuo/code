Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#字符串驻留机制（仅包含下划线（_）、字母和数字）
>>> a="abd_33"
>>> b="abd_33"
>>> a is b  #符合标识符规则，同一个对象
True
>>> id(a)  #地址
54270208
>>> id(b)
54270208
>>> a==b  #值也相等
True
>>> c="dd#"
>>> d="dd#"
>>> c is d  #不是同一个对象
False
>>> id(c)
54269984
>>> id(d)
54271232
>>> c==d  #值相等
True


'''
  ==,判断值相不相等(value)
  is,判断是不是同一个对象(id)
'''


#成员操作符（in/not in）
>>> a="zxcvbnm"
>>> "z" in a
True
>>> "cvb" in a
True
>>> "d" in a
False
>>> "d" not in a
True

#查找方法
>>> a='''学习可以提升我们的技能效率和认知效率。/
技能效率是指应对具体工作场景和问题的方法；/
认知效率是指了解问题本质，了解解决方案的底层规律，/
能够让我们认清楚问题表象背后的实质。/
而大多数人的学习层次停留在提高技能效率上。'''
>>> len(a)   #字符串长度
104
>>> a.startswith("学习")  #指定字符串开头
True
>>> a.endswith("效率上")  #指定字符串结尾
False
>>> a.find("效率")  #找第一次出现指定字符串的位置
11
>>> a.rfind("效率") #找最后一次出现指定字符串的位置
100
>>> a.isalnum()   #所有字符是不是全是字母或数字
False
>>> "asdfg2345".isalnum()  #全是字母或者数字
True


#去除首尾信息
>>> "   a  n  d   ".strip()  #去除首尾空格
'a  n  d'
>>> "*a*n*d*".lstrip("*")  #去除首*
'a*n*d*'
>>> "*a*n*d*".rstrip("*") #去除尾*
'*a*n*d'
>>> "*a*n*d*".strip("*")  #去除首尾*
'a*n*d'


#大小写互换
>>> a="to be or not to be"
>>> a.capitalize()   #产生新的字符串，首字母大写
'To be or not to be'
>>> a.title()        #产生新的字符串，每个字母都大写
'To Be Or Not To Be'
>>> a.upper()        #产生新的字符串，所有字符串转换成大写
'TO BE OR NOT TO BE'
>>> a.lower()        #产生新的字符串，所有字符串转换成小写
'to be or not to be'
>>> a.swapcase()     #产生新的字符串，所有大小字母互换
'TO BE OR NOT TO BE'


#格式排版
>>> a="bnm"
>>> a.center(20,"*")  #20个字符居中，*号补齐
'********bnm*********'
>>> a.center(20)   #20个字符居中
'        bnm         '
>>> a.ljust(20,"*")  #20个字符居中，*号补齐
'bnm*****************' 


'''
  isalnum()  是否为字母或者数字
  isalpha()  检测字符串是否只有字母组成（含汉字）
  isdigit()  检测字符串是否只有数字组成
  isspace()  检测是否为空白符
  isupper()  是否为大小写字母
  islower()  是否为小写字母
'''

