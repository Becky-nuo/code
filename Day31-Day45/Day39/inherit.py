#进一步了解继承（确定一个类是否是另一个类的子类）


#使用内置方法issubclass。
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))



#访问其特殊属性__bases__。(可以了解一个类的基类)
print(SPAMFilter.__bases__)
print(Filter.__bases__)



#使用isinstance(是否是特定类的实例,也可用于类型，如字符串类型（str）)
s = SPAMFilter()  
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))

'''s是SPAMFilter类的（直接）实例，但它也是Filter类的间接实例，因为SPAMFilter是Filter的子类。
            (所有SPAMFilter对象都是Filter对象)   '''



#使用属性__class__。(获悉对象属于哪个类)
print(s.__class__)





'''
    使用isinstance通常不是良好的做法，依赖多态在任何情况下都是更好的选择。
                (一个重要的例外情况是使用抽象基类和模块abc时。)


    对于新式类（无论是通过使用__metaclass__ = type还是通过从object继承创建的）的实例，
还可使用type(s)来获悉其所属的类。对于所有旧式类的实例， type都只是返回instance。
                
''
