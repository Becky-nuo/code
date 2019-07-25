#批量清洗文本数据

import os,re,time
import REdealText import textParse

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
        for folder in folders:     #level directory
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):  #secondary directory
                if os.path.isfile(file_path):
                    this_file = open(file_oath,'rb') #rb读取更快
                    content  = this_file.read().decode('utf8')
                yield catg,content
                this_file.close()


if __name__ == '__main__':
    start = time.time()
    filepath = r'文件路径'
    files = loadFiles(filepath)
    n = 2 #表示抽样
    for i,mag in enumerate(files):
        if i%n == 0:
            catg = msg[0]
            content = msg[1]
            content = textParse(content)  #数据清洗
            if int(i/n) % 5000 ==0:
                print(('{t} *** {i} \t docs has been read'.format(i=1，t=time.strftime('%Y-%M-%D %H:%M:%S),time.localtime())),'\n',catg,"\t",content[:20])



end = time.time()
print("Total Cost Time:%.2f"%(end-start)+'s')
