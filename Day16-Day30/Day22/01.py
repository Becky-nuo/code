#python之导入模块

import math,logging

print(math.log(10)) #调用的是math的log函数
logging.log(10,'something') #调用的是logging的log函数


'''名字冲突可以给函数起个‘别名’来避免冲突'''

from math import log
from logging import log as logger #logger的log现在变成了logger

print(log(10))  #调用的是math的log
logger(10,'import from logging')  #调用的是logging的log


#测试是否存在相应的文件夹和文件
import os
print(os.path.isdir(r'C:\window'))
print(os.path.isfile(r'C:\window\addins\FXSEXT.ecf'))
