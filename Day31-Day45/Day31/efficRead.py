#高效读取文件（coding:utf-8）


import os,time

#迭代器类

class loadFolders(object):
    def __init__(self,par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath=os.path.join(self.par_path,file)
            if os.path.isdir(file_abspath):
                yield file_abspath


class loadFiles(object):
    def __init__(self,par_path):
        self.par_path=par_path
    def __iter__(self):
        folders=loadFolders(self.par_path)
        for folder in folders:
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):
                yield catg,file


if __name__ == '__main__':
    filepath = os.path.abspath(r'文件路径')
    for i,mag in enumerate(files):
        if i%10000 = 0:
            print('{t} *** {i} \t docs has been read'.format(i=1，t=time.strftime('%Y-%M-%D %H:%M:%S),time.localtime()))

    end = time.time()
    print('Total spent times:%.2f' % (end - start) + 's')


'''
    Description:高效读取文本
    Prompt:code in python3 env

'''

                                                                                 
