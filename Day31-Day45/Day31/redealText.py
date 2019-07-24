#正则清洗文本数据（condig=utf-8）

import re

def textParse(str_doc):
    '''正则过滤掉特殊符号、标点、英文、数字等
    r1 - '[a-zA-Z0-9'!"#$%&\'()*+,-./:：;：|<=>?@,-。?、"]^_'{|}~]+'

    #去除空格
    r2 = '\s+'
    str_doc=re.sub(r1.' ',str_doc)
    str_doc=re.sub(r2.' ',str_doc)

    #去除换行符
    str_doc = str_doc.replace('\n',''）
    return str_doc


def readFile(path):
    str_doc = ""
    with open(path,'r',encoding='utf-8') as f:
        str_doc = f.read()
        return str_doc


if __name__ == '__main__':
    path = r'../文本路径'
    str_doc = readFile(path)
    #print(str_doc)


    '''数据清洗'''
    res = textParse(str_doc)
    print(res)

'''
    DESC:正则清洗文本数据
    Author:伏草惟存
    Prompt:code in python3 env
'''
