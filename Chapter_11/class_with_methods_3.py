class employee:
    company = "ITC"
    def showone(self, salary, name):
        self.name = name 
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")

class programmer(employee):
    company = "ITC infotech"
    lang = "java"
    def show(self):
        print(f"name is {self.name} and the salary is {self.salary}")
    
    def showlang(self):
        print(f"Name is {self.name} and the language is {self.lang}")
    

class number:
    a = 43
    @classmethod
    def num(cls):
        print(f"the number is {cls.a}")


a = employee()
b = programmer()
c = number()
print(a.company, b.company)
c.num()