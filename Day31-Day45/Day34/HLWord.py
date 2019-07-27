#自定义选择高低词频

from FreqWord import *
from StopWOrd import *



#选择高低词
def h1_freqword(fdist):
    wordlist = []
    print('=','打印统计词频'，‘=’*3)
    for key in fdist.keys():
        if fdist.get(key)>2 and fdist.get(key)<15:
            wordlist.append(key+':'+str(fdist.get(key))
    return wordlist


if __name__ == '__main__':
    path = r'文本路径.txt'  #读取文本
    str_doc = readFile(path)
    word_list = seg_doc(str_doc)
    print(word_list)


#选择高低词
fdist = nltk_wf_feature(word_list)
fdist = h1_freqword(fdist)
print(fdist)
