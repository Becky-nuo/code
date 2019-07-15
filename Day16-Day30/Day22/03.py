#python之使用__future__

from __future__ import division
print(10/3)
print(10//3)  #整数d



from __future__ import unicode_literals

s = 'am I an unicode?'
print(isinstance(s,unicode))
print(isinstance(s,str))

r = b'am I an unicode?'
print(isinstance(b'r',unicode))
print(isinstance(b'r',str))

