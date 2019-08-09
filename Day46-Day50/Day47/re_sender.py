#找出发件人（使用模块fileinput,找出文件的所有地址）


import fileinput, re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))




import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address)
        for address in sorted(addresses):
            print(address)




'''

程序注意点:
    用正则表达式，可以提高处理效率，
    匹配要提取文本的子模式放在圆括号内，使其变成了一个编组。
    用非贪婪模式，使其只匹配最后一对尖括号（以防姓名也包含尖括号）。
    用美元符号指出要使用这个模式来匹配整行（直到行尾）。
    用if语句来确保匹配后才提取与特定编组匹配的内容。


    排序时大写字母在小写字母之前


    列出邮件头中提及的所有邮件地址，需要创建一个只与邮件地址匹配的正则表达式，
然后使用方法findall找出所有与之匹配的内容。

    为避免重复，可将邮件地址存储在本章前面介绍的合中。最后，提取键，将它们排序并打印出来。


    调用fileinput.close()，可要求找出邮件头中的地址（程序找出了整个文件中的所有地址）。

    邮件头不可能包含空行，如果有多个文件，也可在遇到空行后调用fileinput.nextfile()来处理下一个文件。


'''
