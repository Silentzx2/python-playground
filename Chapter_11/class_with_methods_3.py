class employee:
    company = "ITC"
    def show(self, salary, name):
        self.name = name 
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")

class programmer:
    company = "ITC infotech"
    def show(self):
        print(f"name is {self.name} and the salary is {self.salary}")
    
    def showlang(self):
        print(f"Name is {self.name} and the language is {self.lang}")

a = employee()
b = programmer()
print(a.company, b.company)