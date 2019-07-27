#slearn 计算多类下的TFIDF

from Stopwords import readFile,seg_doc
from sklearn.feature_extraction.text import TfidTransformer
from sklearn.feature_extraction.text import CountVectorizer



#利用sklearn计算tfidf值特征
def sklearn_tfidf_fetturn(corpus=None):
    vectorizer = CountVerctorizer  #构建词汇表
    transformer = TfidfTransformer #该类会统计每个词语的tf_idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    #print(tfids)

    words = vectorizer.get_feature_names() #获取词袋模型中的是所有词语
    weight = tfidf.toarray()  #把tf-idf矩阵抽取出来，元素i,j表示j词在i类文本中的tf-idf权重
    #print(words)
    #print(weight)


    for i in range(len(weight)):
        print(u"-----这里输出第",i,u"类文本的词语tf_idf权重")
        for j in range(len(words)):
            print(words[j],weight[i])
    


if __name__ == '__main__':
    path1 = r'文本路径.txt'  #读取文本
    str_doc1 = readFile(path1)
    word_list1 = ''.join(seg_doc(sttr_doc1))



    path2 = r'文本路径.txt'  #读取文本
    str_doc2 = readFile(path2)
    word_list2 = ''.join(seg_doc(sttr_doc2))

    corpus.append(word_list1)
    corpus.append(word_list2)

    sklearn_tfidf_fetturn(corpus)
