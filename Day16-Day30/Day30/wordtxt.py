#抽取word文档文本内容（coding=utf-8）
'''
    Description:word文档信息提取
    Author:伏草惟存
    prompt:code in python3 env
    
'''

import os,fnmatch

from win32com import client as wc
from wiin32com.client import Dispath
'''
    功能描述：word文件转存txt.默认保存在根目录下，支持自定义
    参数描述：1、filePath(文件路径) 2、savePath(保存路径)
    
'''

def wordTxt(filePath,savePath=''):
    dirs,filename = os.path.split(filePath) #切分文件路径为文件目录和文件名
    print(dirs,'\n',filename)



'''修改切分后的文件后缀'''
new_name=""
if fnmatch.fnmatch(filename,'*.doc'):
    new_name = filename[:-4]+'.txt'

elif fnmatch.fnmatch(filename,'*.docx'):
     new_name = filename[:-5]+'.txt'

else:
    print('格式不正确，仅支持doc or docx 格式')


'''设置新的文件保存路径'''

if savePath=='':
    savePath = dirs

else:
    savePath = savePath
wordtxtPath = os.path.join(savePath,new_name)
print('-->',wordtxtPath)


'''加载文件提取的处理程序。word-->txt'''

worddapp = wc.Dispath('word.Application')
mytxt = wordapp.Documents,Open(filePath)


'''保存文本信息'''
mytxt.SaveAs(wordtxtPath,4)#参数4代表抽取文本
mytxt.Close()
        


if __name__=='__main__':
    filePath = os.path.abspath(r'文本路径.doc')
    filePath = os.path.abspath(r'文本路径.doc')
    wordtxt(filePath)
