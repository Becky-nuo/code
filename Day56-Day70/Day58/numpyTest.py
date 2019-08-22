#ndarray

import numpy as np

def main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    
    np_lst=np.array(lst)
    print(type(np_lst))
    
    np_lst=np.array(lst,dtype=np.float)  #bool,int,int8-128,uint8-128,float,float16/32...
    print(np_lst.shape)  #指明形状
    print(np_lst.ndim)  #指定维数
    print(np_lst.dtype) #数据类型
    print(np_lst.itemsize) #每个维数的大小
    print(np_lst.size)#字节

if __name__=="__main__":
    main()
    
