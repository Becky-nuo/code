#@property装饰器的用法

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_salary(self):   #get方法
        return self.__salary

    def set_salary(self,salary):  #set方法
        if 10000<salary<50000:
            self.__salary = salary
        else:
            print("录入错误！在10000—50000范围")



emp=Employee("小明",30000)
print(emp.get_salary)  #私有
emp.set_salary(20000)
print(emp.get_salary())

