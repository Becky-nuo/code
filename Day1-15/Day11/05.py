#浅拷贝和深拷贝
'''
    浅拷贝（copy）:不拷贝子对象的内容，只是拷贝子对象的引用(个体)
    深拷贝（deepcopy）:会连子对象的内容也全部拷贝一份，对子对象的修改不会影响源对象（全部）
    
'''


#浅拷贝
import copy  #模块


a=[10,20,[5,6]]
b=copy.copy(a)  #浅拷贝


print("a:",a)
print("b:",b)


b.append(30)
b[2].append(7)
print("浅拷贝....")
print("a:",a)
print("b:",b)


print("#################")


#深拷贝
import copy


a=[10,20,[5,6]]
b=copy.deepcopy(a)


print("a:",a)
print("b:",b)


b.append(30)
b[2].append(7)
print("深拷贝....")
print("a:",a)
print("b:",b)

