Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


#str()数字型转字符串
>>> int("123")   #整数
123
>>> float("1.23")   #浮点数
1.23
>>> str(2.20)   
'2.2'
>>> str(234)
'234'
>>> str(22.2e2)  #乘100
'2220.0'



#[]提取字符
>>> a='abcdefghijklmnopqrstuvwxyz'  #0到25
>>> a
'abcdefghijklmnopqrstuvwxyz'
>>> a[0]     #正向  
'a'
>>> a[3]
'd'
>>> a[25]
'z'
>>> a[26]   #超出范围
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[26]
IndexError: string index out of range

>>> a[-1]  #反向搜索  -1到-26
'z'
>>> a[-2]
'y'
>>> a[-26]
'a'
>>> a[-27]  #超出范围
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[-27]
IndexError: string index out of range



#replace()字符串替换
>>> a[0]="嗯"   #字符串是不可变
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[0]="嗯"
TypeError: 'str' object does not support item assignment

>>> a.replace("b","嗯")  
'a嗯cdefghijklmnopqrstuvwxyz'  #新字符串
>>> a   #老字符串
'abcdefghijklmnopqrstuvwxyz'
>>> a=a.replace("b","嗯")
>>> a
'a嗯cdefghijklmnopqrstuvwxyz' #新字符串




 #字符串切片slice操作
>>> a[2]
'c'
>>> a[1:5]   #[1,5),包头不包尾
'嗯cde'
>>> a[1:5:1]   #[1,5),1：一个一个取
'嗯cde'
>>> a[1:5:2]    #[1,5)，2：隔一个取
'嗯d'
>>> a[:]   #取出全部字符串
'a嗯cdefghijklmnopqrstuvwxyz'
>>> a[:3]    #从0开始，到3
'a嗯c'
>>> a[-3]  #反向
'x'
>>> a[-3:]    #倒数第三个
'xyz'
>>> a[-8:-3]   #倒数第八个，倒数第三个，[-8,-3)
'stuvw'
>>> a[::-1]   #从右到左反向提取
'zyxwvutsrqponmlkjihgfedc嗯a'
>>> a[2:30]   #超出范围会在最大值停住，不会报错
'cdefghijklmnopqrstuvwxyz'


>>> "to be or not to be"[::-1]  #倒序输出
'eb ot ton ro eb ot'


#split()分割和join()合并
>>> b="to be or not to be"
>>> b.split()  #分割成多个子字符串
['to', 'be', 'or', 'not', 'to', 'be']
>>> b.split("be")  #切割掉be
['to ', ' or not to ', '']


>>> c=["s,s100,s200,s300"] 
>>> '*'.join(c)   #拼接，*是连接符（可加可不加），比+性能高
's,s100,s200,s300'




