# 基于python结巴分词，调用自定义词库已经去除停用词（coding: utf-8）

import time
import jieba
import jieba.posseg as pseg#用于词性标注
#分词

#停用词过滤
def stop_word(fid1,fid2,fid3):
    stopword=[]
    for j in fid2.readlines():
        stopword.append(j.strip().decode("utf-8"))#储存停用词表
        #print j
    for i in fid1.readlines():
        data_line=i.strip()
        wordList = jieba.cut(data_line.decode("utf-8"))#wordlist是一个生成器
        outStr=''
        for word in wordList:
            if word not in stopword:
                outStr+=word
                outStr+=' '
        fid3.write(outStr.strip().encode('utf-8') + '\n')

#主文件
def main():
    jieba.enable_parallel()
    # 加入自定义词库
    jieba.load_userdict("文本路径.txt")
    t1 = time.time()
    fid1=open('文本路径.txt','r')#读取文件
    fid2=open('文本路径.txt','r')#读取停用词表
    fid3=open('文本路径.txt','w')#将要写入的文件
    stop_word(fid1,fid2,fid3)#停用词过滤

    fid1.close()
    fid2.close()
    fid3.close()
    t2 = time.time()
    tm_cost = t2-t1
    print tm_cost

main()
