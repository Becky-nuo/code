#递归遍历读取数(coding=utf-8)

import os,time


#遍历目录文件
def TraversalDir(rootDir):
#返回指定目录包含的文件或文件夹的名字的列表
    for i,lists in enumerate(os.listdir(rootDir)):
        path=os.path.join(rootDir,lists) #待处理文件夹名字列表
        if os.path.isfile(path): #核心算法，对文件具体操作
            if i%10000 ==0:
                print('{t} *** {i} \t docs has been read'.format(i=1.strftime('%Y-%M-%D %H:%M:%S),time.localtime())))
            pass


#递归遍历文件目录
if os.path.isdir(path):
    TraversalDir(path)



if __name__== '__main__':
    t1 = time.time()
    rootDir = r'文件路径'
    t2 = time.time
    print('Total Cost Time %.2f' %(t2-t1))


'''
    DESC:递归批量读取30w新闻文件
    Author:伏草惟存
    Promot:
    Code in python3 env


    功能描述：遍历目录，对子文件单独处理

'''
