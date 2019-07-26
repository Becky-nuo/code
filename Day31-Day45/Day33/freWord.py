#文本词频分析

import jieba
txt=open("threekingdoms.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:  #排除单个字符的分词结果
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))



'''输出结果中，出现了“玄德”、“玄德曰”，/
应该为同一个人但jieba划分为两个词汇，这种情况需要整合处理'''
 
excludes={"将军","却说","二人","不可","荆州","不能","如此"}
import jieba
txt=open("threekingdoms.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}


for word in words:
    if len(word)==1:  #排除单个字符的分词结果
        continue
    
    elif word=="诸葛亮"or word=="孔明曰":
        rword="孔明"
        
    elif word=="关公"or word=="云长":
        rword="关羽"
        
    elif word=="玄德"or word=="玄德曰":
        rword="刘备"
        
    elif word=="孟德"or word=="丞相":
        rword="曹操"
        
    else:
        rword=word
        counts[word]=counts.get(word,0)+1

        
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
