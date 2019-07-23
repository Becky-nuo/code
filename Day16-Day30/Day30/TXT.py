#遍历文件抽取TXT文件


import glob
import os
import tensorflow as tf
import numpy as np
import pandas as pd
 
path=r'C:\Users\Python'
f =r'C:\Users\Python\new_file.txt'
 
# read all txt files and save all columns to new_file
def read_writeFile(path,f):
#    cate=[path+'/'+x for x in os.listdir(path)]
    cate=[x for x in os.listdir(path)]
    f2 = open(f, 'a+')
    for idx,folder in enumerate(cate):
        for im in glob.glob(folder+'/*.txt'):
            f1 = open(im, 'r')
            for eachLine in f1:
                f2.write(eachLine)
                f2.write(' '+str(idx+1)+'\n')             
            f1.close()         
 
read_writeFile(path,f)
