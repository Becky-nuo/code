#@property的最简用法


class Employee:

    @property     #装饰器
    def salary(self):
        print("salary run...")
        return 10000



emp=Employee()
print(emp.salary)
