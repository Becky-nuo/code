#正则表达式(coding:utf-8)

import re



line = r'python: 数据预处理'

rege_str1 = '^t.*'  #开头+任意次数
rege_str2 = '.*?(s+)'
rege_ste3 = '.*([\u4E00-\u9FA45]+数)' #提取汉字
rege_ste4 = '.*(\d{4}年)'


res = re.match(rege_str1,line)
if res:
    print(res)
    print(res.group(1))
else:
    print('python')




'''日期提取'''
#line = '小明出生于1999年1月1日'
#line = '小红出生于1999-10-1'
line = '小张出生于1999-10-01'
#line = '李四出生于1999/10/1'
#line = '张三出生于1999-10'


rege_str = '.*出生于（\d{4}[年/-1]\d{1,2}([月/-]\d{1,2}|[月/-]$|$)）'
res= re.match(rege_str,line)
if res:
    print(res)
    print(res.group(1))
else:
    print('python')



'''
常见表达式：
        .   任意字符
        
        *   任意次数
        
        ^   表示开头

        $   表示结尾

        ？  非贪婪模式，提取第一个字符

        +   至少出现一次

        \d    匹配数字

        |     或的关系

        []    满足任意一个都可以，[2345]任意[0-9]区间  [^1]非1

        \s    为空格

        \S    为非空格

        \w    匹配[A-Za-z0-9]

        \W    反匹配[A-Za-z0-9]

        [\u4E00-\u9FA5]  汉字匹配

        {1}      出现一次
        {3,}     出现3次以上
        {2,5}    最少出现2次最多5次
