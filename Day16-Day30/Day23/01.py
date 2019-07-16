#python 中初始化实例属性

class Person(object):
    def __init__(self,name,gender,birth):
        self.name = name
        self.gender = gender
        self.birth = birth

xiaoming = Person('Xiao Ming','Male','2000-1-1')
xiaohong = Person('Xiao Hong','Female','2015-5-5')

print(xiaoming.name)
print(xiaohong.birth)



class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.items():
            setattr(self,k,v)
        
xiaoming = Person('Xiao Ming','Male','2000-1-1',jon='Student' )
print(xiaoming.name)
print(xiaoming.job)


'''
    1、__init__()方法的第一个参数必须是self(也可以用别的名字，但建议使用习惯用法)
    2、我们可以自由地给一个实例绑定各种属性，但一种类型的实例应该拥有相同的名字属性。
    
'''    
