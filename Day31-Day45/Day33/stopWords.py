#自定义去停用词

#正则对字符串清洗
def textParse(str_doc):
    str_doc = re.sub('\u3000','',str_doc)  #去掉字符
    str_doc = re.sub('\s+','',str_doc)  #
    str_doc = str_doc.replace('\n','')  #

    
    r1 = '[a-zA-Z0-9'!"#$%&\'()*+,-./:：;：|<=>?@,-。?"]^_{|}~]+'
    str_doc = re.sub(r1,'',str_doc)
    return str_doc


#创建停用词列表
def get_stop_words(path = r'停用词文本路径.txt'):
    file = open(path,'r',encoding = 'utf-8').resd().split('\n')
    return set(file)


#去掉一些停用词和数字
def rm_tokens(words,stwlist):
    words_list = list(words)
    stop_words = stwlist

    for i in range(word_list.__len__())[::-1]:
        if words_list[i] in stop_words: #去掉停用词
            word_list.pop(i)
        elif words_list[i].isdigit(): #去掉数字
            words_list.pop(i)
        elif len(words_list[i]) == 1 : #去掉单个字符
            words_list.pop(i)
        elif words_list[i] ==" " : #去掉空字符
            words_list.pop(i)

    return words_list


#利用jieba对文本进行分词，返回切词后的list
def seg_doc(str_doc):
    sent_list = str_doc.split('\n')  #正则处理原文件
    sent_list = map(textParse,sent_list)
    stwlist = get_stop_words()  ##获取停用词
    word_2dlist = [rm_tokens(jieba.cut(part,cut_all=False),stwlist)sent list]#分词并去掉停用词
    word_list = sum(word_2dlist,[])  #合并列表
    return word_list
    
    


if __name__ =='__main__':
    path = r'文件路径.txt'
    str_doc = readFile(path)
    #print(str_doc)

    word_list =seg_doc(str_doc)
    print(word_list)
