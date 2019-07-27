#文本特征提取

from Stopwords import resfFile,seg_doc
import os,time


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



if __name__ = '__main__':
    startime = time.time()
    
    filepath= os.path.abspath(r'...文本路径.txt')
    files = loadFolders(filepath)
    n = 5  #
    for i,msg in enumerate(files):
        if i % n == 0
        catg = msg[0]
        file = msg[1]
        file = seg_doc(content)
        if int(i%n) % 2000 == 0:
            print('{t}***{i} \t docs has been dealed'.format(i=i,t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())),'\n',catg,'\t',file[:20])

        
        
    
    

    endTime = time.time()
    print('toal spent times:%.2F' % (endTime-startTime)+ 's')
