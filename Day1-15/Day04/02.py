
#切片

s = 'hello'
print(s[0:3])     #显示下标0到下标3的字符        (hel)
print(s[0:4:2])   #（start:end:step)             (hl)
print(s[-1])      # 显示倒数第一个字符           (o)
print(s[:2])      #显示前两位字符                (he)
print(s[:-1])     #显示倒数第一个之前的所有字符  (hell)
print(s[::-1])    #倒序输出                      (olleh)
print(s[1:])	  #显示第一个字符除外的其他字符  (ello)
print(s[:])       # 显示所有字符                 (hello)
