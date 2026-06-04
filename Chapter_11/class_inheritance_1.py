class employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.company}")


class coder:

    def printlang(self, code):
        self.lang = self.lang
        print(f"the lang is {self.lang}")

    def printtxt(self):
        print("i am just a robot")


class programmer(employee, coder): # You can use like if you want to use multiple classes in one
    company = "tesla"
    lang = "java"
    def show(self):
        print(f"the company is {self.company} and the language is {self.lang}")

# Create objects (instances) from classes using ().
# Earlier, `a = programmer` stored the class itself, so calling `a.show()`
# had no instance to pass as `self`, which caused:
# TypeError: programmer.show() missing 1 required positional argument: 'self'
a = programmer()
b = employee()
c = coder()
a.show()
a.printtxt()
