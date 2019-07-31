
#封装



o = Openobject() # 对象就是这样创建的(（通过像调用函数一样调用类）)
o.set_name('Sir Lancelot')
print(o.get_name())


global_name='Sir Lancelot'

global_name = 'Sir Gumby'
print(o.get_name())



o1 = OpenObject()  #尝试创建多个OpenObject对象
o2 = OpenObject()  #设置一个对象的名称时，将自动设置另一个对象的名称。
o1.set_name('Robin Hood')
print(o2.get_name())


c = ClosedObject()  #不能证明名称不是存储在全局变量中的。
c.set_name('Sir Lancelot')
print(c.get_name())


r = ClosedObject()
r.set_name('Sir Robin')  #从中可知正确地设置了新对象的名称
print(r.get_name())


print(c.get_name())





'''
    封装让你无需知道对象的构造就能使用它
    封装（ encapsulation）指的是向外部隐藏不必要的细节（无需知道对象的内部细节就可使用它）。
    封装不同于多态,多态让你无需知道对象所属的类（对象的类型）就能调用其方法。
    如果你使用属性而非全局变量重新编写前面的类，并将其重命名为ClosedObject，

    属性是归属于对象的变量，就像方法一样。
    方法差不多就是与函数相关联的属性

    对象的方法可能修改这些属性，因此对象将一系列函数（方法）组合起来，
并赋予它们访问一些变量（属性）的权限，而属性可用于在两次函数调用之间存储值。
'''
