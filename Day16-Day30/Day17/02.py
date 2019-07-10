#运算符的重载

class Person:
    def __init__(self,name):
        self.name=name



    def __add__(self,other):
        if isinstance(other,Person):
            return "{0}——{1}".format(self.name,other.name)
        else:
            return "不同类型对象，不能相加"


    def __mul__(self,other):
        if isintance(other,int):
            return self.name*other
        else:
            return "不同类型对象，不能相乘"


p1=Person("小明")
p2=Person("小李")

x = p1 + p2
print(x)


print(x*3)


''' 1、python的运算符实际是通过调用对象的特殊方法实现的
    2、运算符的特殊方法汇总：

         运算符            特殊方法            说明
     
         运算符+           _add_               加法
         运算符-           _sub_               减法
         <,<=,==           _lt_,_le_,_eq_      比较运算符
         >,>=,!=           _gt_,_ge_,_ne_      比较运算符
         |,^,&             _or_,_xor_,_and_    或，异或，与
         <<,>>             _lshift_,rshift_    左移，右移
         *,/               _mul_,_truediv_     乘，浮点除
         %,//              _mod_,_floordiv_    模运算（取余），整数除
         **                _pow_               指数运算


    3、常见特殊方法统计：

        方法               说明                 例子

        __init__           构造方法             对象创建：p=Person()
        __del__            析构方法             对象回收
        __repr__,__str__   打印，转换           print(a)
        __call__           函数调用             a()
        __getattr__        点号运算             a.xxx
        __setattr__        属性赋值             a.xxx=value
        __getitem__        索引运算             a.[key]
        __setitem__        索引赋值             a[key]=value
        __len__            长度                 len(a)
'''
