#文本词频分析（英）

import jieba

def getText():
    txt=open("hmlt.txt","r").read() #打开文件
    txt=txt.lower()                  #将所有单词转换为小写去掉大小写的干扰
    for ch in '`!@#~$%^&*()_+-=*/{}[];,./?<>': #去掉所有的特殊符号
        txt=txt.replace(ch," ")   #将特殊符号替换成空格 即去掉
    return txt


hmltTxt=getText()    #对文件进行读取
words=hmltTxt.split()

#因为现在单词间均为空格分隔开来，所以用split用空格分隔他们并变成列表返回
counts={} #建立一个字典

for word in words:
    counts[word]=counts.get(word,0)+1
    
#用当前的某一个单词作为键索引字典 如果在里面则返回次数再加一 若不在里面则直接加1
items=list(counts.items())

#用list将counts变为一个列表类型  counts.items()-->返回可遍历的（键，值）元组数组
items.sort(key=lambda x:x[1],reverse=True)


#使用list.sort()方法来排序，此时list本身将被修改
for i in range(100):
    word,count=items[i]         
    print("{0:<10}{1:>5}".format(word,count))


'''从输出结果来看，高频单词大多数是冠词，代词、连接词等词汇，/
并不能代表文章的含义进一步的可以采用集合类型构建一个排除词汇库excludes，/
在输出结果中排除这个词汇库中的内容'''
 
excludes={"the","and","of","you","a","with","but","as","be","in","or","are"}
 
def getText():
    txt=open("hmlt.txt","r").read() 
    txt=txt.lower()                 
    for ch in '`!@#~$%^&*()_+-=*/{}[];,./?<>':
        txt=txt.replace(ch," ")  
    return txt


hmltTxt=getText()  
words=hmltTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]         
    print("{0:<10}{1:>5}".format(word,count))
