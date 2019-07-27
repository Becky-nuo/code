#命名实体提取（人名、地名、...）

import jieba.posseg as ps
from StopWords import *


def extract_featurw(str_doc):
    featWord = ""
    stwlist = get_stop_words()
    user_pos_list = ['nr','ns','nt','nz']  #自定义特征词性列表
    for Word,pos in ps.cut(str_doc):
        if word not in stwlist and pos in user_pos_list:
            if word+' '+pos+'\n' not in frstword:
                festword += word+' '+pos+'\n'
    print('命名实体识别：'，featword)
    return featword
        
    

if __name__ == '__main__':
    path = r'文本路径.txt'  #读取文本
    str_doc = readFile(path)
    print(extract_featurw(str_doc))
