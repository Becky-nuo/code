#模块re(包含多个使用正则表达式的函数)

import re


if re.search(pat, string):
    print('Found it!')


some_text = 'alpha, beta,,,,gamma delta'
print(re.split('[, ]+', some_text))



re.split('[, ]+', some_text, maxsplit=2)  #参数maxsplit指定最多分割多少次
re.split('[, ]+', some_text, maxsplit=1)


pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat, text))


pat = r'[.?\-",]+'
print(re.findall(pat,text))



pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat, 'Mr. Gumby', text))



re.escape('网址')
print(re.escape('But where is the ambiguity?'))



'''
    模块re中一些重要的函数

            函 数                                             描 述
        compile(pattern[, flags])               根据包含正则表达式的字符串创建模式对象
        search(pattern, string[, flags])        在字符串中查找模式
        match(pattern, string[, flags])         在字符串开头匹配模式
        split(pattern, string[, maxsplit=0])    根据模式来分割字符串
        findall(pattern, string)                返回一个列表，其中包含字符串中所有与模式匹配的子串
        sub(pat, repl, string[, count=0])       将字符串中与模式pat匹配的子串都替换为
        replescape(string)                      对字符串中所有的正则表达式特殊字符都进行转义


函数re.compile将用字符串表示的正则表达式转换为模式对象，以提高匹配效率。

调用search、 match等函数时，如果提供的是用字符串表示的正则表达式，都必须在内部将它们转换为模式对象。

通过使用函数compile对正则表达式进行转换后，每次使用它时都无需再进行转换。

模式对象也有搜索/匹配方法，re.search(pat, string),模式对象搜索/匹配方法。
（其中pat是一个使用字符串表示的正则表达式）等价于pat.search(string)（其中pat是使用compile创建的模式对象）。

编译后的正则表达式对象也可用于模块re中的普通函数中。

函数re.search在给定字符串中查找第一个与指定正则表达式匹配的子串。

要找子串，将返回MatchObject（结果为真），否则返回None（结果为假）。

函数re.match给定字符串开头查找与正则表达式匹配的子串。

函数re.split根据与模式匹配的子串来分割字符串。这类似于字符串方法split，但使用正则表达式来指定分隔符，而不是指定固定的分隔符。

函数match在模式与字符串开头匹配时就返回True，而不要求模式与整个字符串匹配。

函数re.findall返回一个列表，其中包含所有与给定模式匹配的子串。

函数re.sub从左往右将与模式匹配的子串替换为指定内容。

连字符（ -）进行了转义，因此Python不会认为它是用来指定字符范围的（如a-z）。

re.escape是一个工具函数，用于对字符串中所有可能被视为正则表达式运算符的字符进行转义。



'''
