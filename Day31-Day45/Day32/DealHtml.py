#清洗HTML的数据（conding=utf-8）

import re


#@param htmlstr HTML字符串
def filter_tags(htmlstr):
    htmlstr = ''.join(htmlstr.split())  #去除多余空格
    re_doctype = re.compile(r'<!DOCTYPE .*?>',re.S)
    res = re_cdata.sub('',res)


    #Script
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*script\s*>',re.I)
    res = re_script.sub('',res)


    #style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)
    res = re_style.sub('',res)  #去掉style


    #处理换行
    re_br = re.compile('<br\s*?/?>')
    res = re_br.sub(''.res)  #将br转换为换行


    #HTML标签
    re_h = re.compile('</?\w+[^>]*>')
    res = re_h.sub('',res) #去掉HTML标签


    #多余的空行
    blank_line = re.compile('\n+')
    res = blank_line.sub('',res)

    blank_line_1 = re.compile('\n')
    res = blank_line_1.sub('',res)
    

    return res


def readFile(poth):
    str_doc = ""
    with open(path,'r',encoding='utf-8') as f:
        str_doc = f.read()

    return  str_doc


if __name__ = '__main__':
    str_doc = readFile(r'文件路径')
    res = filter_tags(str_doc)
    print(res)


'''
        re.I   使匹配对大小写不敏感
        re.L   做本地化识别（locale-awaare）匹配
        re.M   多行匹配，影响^和$
        re.S   使 . 匹配包括换行在内的所有字符
        re.U   根据Unicode字符集解析字符。这个标志影响 \w \W \b \B
        re.X   该标志通过给予你更灵活的格式以便你将正则表达式写的更易懂

'''

