#jieba分词


import jieba

#结巴中文分词基本操作

print('='*40)
print('1.分词')
print('-'*40)

#全模式，扫描所有可以成词的词语

seg_list = jieba.cut('无论你多富有，无论你官多大，角色就是人格',cut_all=True)
print('Full Mode:'+','.join(seg_list))


#默认是精确模式，适合文本分析
seg_list = jieba.cut('无论你多富有，无论你官多大，角色就是人格',cut_all=False)
print('Default Mode:'+','.join(seg_list))

#搜索引擎模式，对长词再次切分，提高召回率
seg_list = jieba.cut_for_search('无论你多富有，无论你官多大，角色就是人格',HMM=True)
print('搜索引擎模式:'+','.join(seg_list))


print('='*40)
print('2.添加自定义词典、调整词典')
print('-'*40)


seg_list=jieba.cut('如果放到数据库中将出错')
print('原文档：\t'+'/'.join(seg_list))
print(jieba.suggest_freq('中','将'),True)
print('改进文档：\t'+'/'.join(seg_list,HMM=False))
